from agents.base import PrismAgent
from agents.prompts import WorkerPrompt
from message import Message

class WorkerAgent(PrismAgent):

    def setup(self):
        prompt = WorkerPrompt.from_args(
            tools=[v for _, v in self._tools.items()],
            description=self._description,
        )
        # System message
        self._system_message = Message(
            role="system",
            content=prompt.compiled,
        )
        self._set_initial_conversation()
