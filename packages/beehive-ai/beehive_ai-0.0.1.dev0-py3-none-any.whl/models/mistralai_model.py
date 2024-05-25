import logging

from models.base import Model


# Logger
logger = logging.getLogger(__file__)


class MistralAIModel(Model):
    _client: "MistralClient"  # type: ignore

    def _create_client(self, **client_kwargs) -> "MistralClient":  # type: ignore
        from mistralai.client import MistralClient
        self._client = MistralClient(**client_kwargs)
        return None