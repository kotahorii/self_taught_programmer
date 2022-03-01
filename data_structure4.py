from ctypes import Union
from typing import Any, Literal


class MinStack:
    def __init__(self) -> None:
        self.main: list[Any] = []
        self.min: list[Any] = []

    def push(self, n: Any) -> None:
        if len(self.main) == 0:
            self.min.append(n)
        elif n <= self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.min[-1])
        self.main.append(n)

    def pop(self):
        self.min.pop()
        return self.main.pop()

    def get_min(self):
        return self.min[-1]


def check_parentheses(a_string: str) -> bool:
    stack: list[str] = []
    for c in a_string:
        if c == "(":
            stack.append(c)
        if c == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0
