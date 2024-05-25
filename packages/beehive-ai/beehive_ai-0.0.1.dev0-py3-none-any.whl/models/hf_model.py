import os
from os import PathLike
from typing import Any, Callable

from models.base import Model


# TODO (Mihir) update this class
class HfModel(Model):
    _tokenizer: "AutoTokenizer"  # type: ignore
    _client: "AutoModelForCausalLM"  # type: ignore

    def __init__(self,
        name: str,
        model: str,
        temperature: int = 0,
        agent_prompt: str = "You are a helpful assistant.",
        tools: list[Callable[..., Any]] | None = None,
        system_prompt: str | None = None,
        conversation_fpath: PathLike | None = None,
        huggingfacehub_api_token: str | None = None,
        **model_kwargs
    ):
        if not huggingfacehub_api_token:
            huggingfacehub_api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN", None)
        if not huggingfacehub_api_token:
            raise ValueError((
                "To use this class, you should have installed the `huggingface_hub` package,"
                " created an user access token, and set the environment variable `HUGGINGFACEHUB_API_TOKEN`"
                " with your token or passed it as a named parameter to the constructor."
            ))
        
        super().__init__(
            name,
            model,
            temperature,
            agent_prompt,
            tools,
            system_prompt,
            conversation_fpath,
            **model_kwargs
        )

    def _create_model_client(self, **kwargs) -> None:
        from transformers import (
            AutoTokenizer,
            AutoModelForCausalLM,
            set_seed
        )
        self._tokenizer = AutoTokenizer.from_pretrained(self._model, use_fast=False)
        self._client = AutoModelForCausalLM.from_pretrained(
            self._model,
            **kwargs
        )
        set_seed(self._temperature)
