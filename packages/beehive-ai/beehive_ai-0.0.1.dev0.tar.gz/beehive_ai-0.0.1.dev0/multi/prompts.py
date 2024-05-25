from agents.base import PrismAgent
from agents.prompts import Prompt


class SupervisorPrompt(Prompt):

    @property
    def template(self):
        return (
            "You are a supervisor tasked with managing a conversation between workers."
            " The workers are listed below in the format '<name>: <purpose>':"
            " \n{agent_descriptions}\n"
            "Given the following user request, respond with the worker to act next."
        )
    
    @classmethod
    def from_args(cls,
        agents: list[PrismAgent]
    ):
        return cls(
            agent_descriptions = "\n".join([f"{a.name}: {a._description}" for a in agents]),
        )


class SupervisorNextAgentPrompt(Prompt):

    @property
    def template(self):
        return (
            "Given the conversation above, who should act next?"
            " Select one of: {agent_options}, or FINISH. Make sure to explain your selection.:"
            " ALWAYS give your response as a valid JSON with the following keys:"
            ' {"agent": ..., "reason": ...}.'
        )
    
    @classmethod
    def from_args(cls,
        agent_options: str
    ):
        return cls(
            agent_options=agent_options
        )


class SupervisorFinalAnswerPrompt(Prompt):

    @property
    def template(self):
        return (
            'Based on the conversation, what is the final answer the the initial question:'
            ' "{task}". Answer in a complete sentence. Do not reference'
            ' the conversation in any way. Use all tool calls and their content, if needed.'
        )
    
    @classmethod
    def from_args(cls,
        task: str
    ):
        return cls(
            task=task
        )
