from typing import Any

from message import Message, ToolMessage
from tools.base import Tool


class Model:
    _model: str
    _client_kwargs: dict[str, Any]
    _client: Any

    def __init__(self,
        model: str,
        **client_kwargs,
    ) -> None:
        self._model = model
        self._client_kwargs = client_kwargs
        self._client = self._create_client(**client_kwargs)
    
    def _create_client(self, **client_kwargs):
        raise NotImplementedError()
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self):
        return ValueError("Do not modify the `model` property!")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(model='{self._model}')"
    
    def chat(self,
        user_input: str | None,
        temperature: int,
        tools: list[Tool],
        conversation: list[Message | ToolMessage],
    ):
        raise NotImplementedError()

    def chat_from_message(self,
        message: Message | None,
        temperature: int,
        tools: list[Tool],
        conversation: list[Message | ToolMessage],
    ):
        raise NotImplementedError()
