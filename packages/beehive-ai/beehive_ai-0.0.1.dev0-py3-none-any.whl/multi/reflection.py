import json
import logging

from agents.base import PrismAgent
from agents.prompts import Prompt
from models.base import Model
from message import Message
from output import ConsoleManager


logger = logging.getLogger(__file__)


class Reflexion():
    name: str
    _actor_agent: PrismAgent
    _reflection_agent: PrismAgent
    _state: list[Message]
    
    def __init__(self,
        name: str,
        actor_agent: PrismAgent,
        reflection_agent: PrismAgent,
    ):
        self._name = name
        self._actor_agent = actor_agent
        self._reflection_agent = reflection_agent

        # Create a state. Each agent maintains their own conversations. The state
        # enables agents to share outputs and message with one another.
        self._state: list[Message] = []

    def invoke(self,
        task: str,
        reflection_prompt: str | Prompt = "Evaluate the accuracy of the previous response.",
        recursion_limit: int = 100,
    ):
        trajectory = self._actor_agent.invoke(task)
        self._state.extend(trajectory)
        self._reflection_agent._conversation.extend(trajectory)
        improvements = self._reflection_agent.invoke(reflection_prompt)
        return trajectory, improvements
