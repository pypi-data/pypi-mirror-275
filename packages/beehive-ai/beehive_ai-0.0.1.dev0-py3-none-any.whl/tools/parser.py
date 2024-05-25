from typing import Any, Callable


class FunctionParser:

    def __init__(self, func: Callable[..., Any]):
        self.func = func

