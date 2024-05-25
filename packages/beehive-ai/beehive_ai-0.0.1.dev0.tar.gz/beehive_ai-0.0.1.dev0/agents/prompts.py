
from tools.base import Tool


class Prompt:

    def __init__(self, **template_kwargs):
        self._compiled = self.template.format(**template_kwargs)

    @property
    def template(self):
        raise NotImplementedError()

    @property
    def compiled(self):
        return self._compiled
    
    @compiled.setter
    def compiled(self):
        raise ValueError("Cannot modify `compiled` property directly!")
    

class WorkerPrompt(Prompt):

    @property
    def template(self):
        return (
            "You are a helpful AI assistant. You are one of several assistants collaborating"
            " on this task, and you all are managed by a supervisor. Use the provided tools"
            " to progress towards answering the question. If you are unable to fully"
            " answer, that's OK. You will send your progress to the supervisor, and the"
            " supervisor will call upon another assistant with different tools to help"
            " where you left off. Execute what you can to make progress. If you or any other"
            " assistants have the final answer or deliverable, prefix your response with"
            " FINAL ANSWER so the team knows to stop."
            "\n\n"
            "You have access to the following tools: {tools}. Your job is as follows:"
            " {description}."             
        )
    
    @classmethod
    def from_args(cls,
        tools: list[Tool],
        description: str,
    ):
        return cls(
            tools=', '.join([x.name for x in tools]),
            description=description,
        )
