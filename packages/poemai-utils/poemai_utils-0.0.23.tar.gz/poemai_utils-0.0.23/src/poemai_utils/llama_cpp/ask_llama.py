import asyncio
import base64
import json
import logging
from pathlib import Path
from types import SimpleNamespace
from typing import AsyncGenerator, Iterator

import httpx
import openai
import sqlitedict
from poemai_utils.basic_types_utils import linebreak, short_display
from poemai_utils.utils_config import get_config_by_key

_logger = logging.getLogger(__name__)


def current_unix_time():
    import datetime
    import time
    from types import SimpleNamespace

    unix_timestamp = int(time.time() * 1000)
    dt = datetime.datetime.fromtimestamp(unix_timestamp / 1000)
    # Convert datetime object to ISO date format
    iso_date = str(dt.isoformat())

    return SimpleNamespace(unix_timestamp=unix_timestamp, dt=dt, iso_date=iso_date)


class AskLlama:
    def __init__(
        self, model_path=None, n_ctx=2048, use_gpu=False, prompt_formatter=None
    ):
        try:
            from llama_cpp import Llama
        except ImportError:
            raise ImportError(
                "llama_cpp not installed - use pip install llama-cpp-python"
            )

        if model_path is None:
            model_path = get_config_by_key("LLAMA_MODEL_PATH")
            if model_path is None:
                raise ValueError("LLAMA_MODEL_PATH is not set")

        if prompt_formatter is None:
            self.prompt_formatter = lambda x: x
        else:
            self.prompt_formatter = prompt_formatter

        self.llama_model = Llama(
            model_path=model_path,
            n_gpu_layers=-1 if use_gpu else 0,  # Uncomment to use GPU acceleration
            n_ctx=n_ctx,
        )

        self.model = SimpleNamespace(name="llama")

    @staticmethod
    def prompt_formatter_mixtral():
        return lambda prompt: "[INST] " + prompt + " [/INST]"

    def count_tokens(self, text):
        """Returns the number of tokens in a text string."""
        encoding = self.llama_model.tokenize(text.encode("utf-8"))
        num_tokens = len(encoding)
        return num_tokens

    def ask_completion(
        self,
        prompt,
        temperature=0,
        max_tokens=600,
        stop=None,
        suffix=None,
        system_prompt=None,
        messages=None,
        json_mode=False,
    ):
        if system_prompt is not None:
            print(f"Warning: system_prompt is not supported for {self.llama_model}")
        if messages is not None:
            print(f"Warning: messages is not supported for {self.llama_model}")

        if stop is None:
            stop = []

        logits_processors = None

        if json_mode:
            from llama_cpp import LogitsProcessorList
            from lmformatenforcer.integrations.llamacpp import (
                build_llamacpp_logits_processor,
            )

            logits_processors = LogitsProcessorList(
                [
                    build_llamacpp_logits_processor(
                        self._tokenizer_data(), self._character_level_parser()
                    )
                ]
            )

        output = self.llama_model.create_completion(
            self.prompt_formatter(prompt),
            max_tokens=max_tokens,
            stop=stop,
            echo=False,
            stream=False,
            logits_processor=logits_processors,
        )

        return output["choices"][0]["text"]

    def ask(
        self,
        prompt,
        temperature=0,
        max_tokens=600,
        stop=None,
        suffix=None,
        system_prompt=None,
        messages=None,
        json_mode=False,
    ):
        answer = self.ask_completion(
            prompt,
            temperature,
            max_tokens,
            stop,
            suffix,
            system_prompt,
            messages,
            json_mode,
        )

        return answer

    async def ask_async(
        self,
        prompt,
        temperature=0,
        max_tokens=600,
        stop=None,
        system_prompt=None,
        messages=None,
        metadata=None,
    ) -> AsyncGenerator[dict, None]:
        if system_prompt is not None:
            print(f"Warning: system_prompt is not supported for {self.llama_model}")
        if messages is not None:
            print(f"Warning: messages is not supported for {self.llama_model}")

        if stop is None:
            stop = []

        generator = self.llama_model.create_completion(
            self.prompt_formatter(prompt),
            max_tokens=max_tokens,
            stop=stop,
            echo=False,
            stream=True,
        )

        # Adapt the synchronous generator for asynchronous iteration
        async for part in self._adapt_sync_gen_to_async(generator):
            _logger.debug(f"part: {part}")
            part_content = part.get("choices")[0]["text"]
            yield {"content": part_content}

        _logger.info(f"Finished async ask")

    async def _adapt_sync_gen_to_async(self, sync_gen):
        loop = asyncio.get_running_loop()

        while True:
            try:
                # Offload blocking call to executor
                next_item = await loop.run_in_executor(
                    None, next, sync_gen, StopIteration
                )
                if next_item is StopIteration:
                    break  # Properly terminate async iteration
                yield next_item
            except StopIteration:
                # This block may not be necessary if you use the default sentinel value as shown above
                break  # Ensure proper termination if StopIteration is raised

    def print_log(self, limit=10):
        for key in list(sorted(self.gpt_log.keys()))[-limit:]:
            entry = self.gpt_log[key]
            print(f"----------------------")
            print(f"model: {entry['model']} time: {entry['iso_date']} ")
            print(f"------ PROMPT  -------")
            print(f"{linebreak(entry['prompt'])}")
            print(f"------ ANSWER  -------")
            print(f"{linebreak(entry['answer'])}")
            print(f"**********************")

    def _tokenizer_data(self):
        from lmformatenforcer.integrations.llamacpp import (
            build_token_enforcer_tokenizer_data,
        )

        if self.tokenizer_data is None:
            self.tokenizer_data = build_token_enforcer_tokenizer_data(self.llama_model)
        return self.tokenizer_data

    def _character_level_parser(self):
        from lmformatenforcer import JsonSchemaParser

        if self.character_level_parser is None:
            self.character_level_parser = JsonSchemaParser(None)
        return self.character_level_parser
