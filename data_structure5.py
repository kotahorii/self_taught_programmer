from typing import Any


def check_parentheses(a_string: str) -> bool:
    stack: list[str] = []
    for c in a_string:
        if c == "(" or c == "{":
            stack.append(c)

        if c == ")":
            if len(stack) == 0:
                return False
            if stack[-1] != "(":
                return False
            stack.pop()

        if c == "}":
            if len(stack) == 0:
                return False
            if stack[-1] != "{":
                return False
            stack.pop()
    return len(stack) == 0


class MaxStack:
    def __init__(self) -> None:
        self.main: list[Any] = []
        self.max: list[Any] = []

    def push(self, n: Any) -> None:
        if len(self.main) == 0:
            self.max.append(n)
        elif n >= self.max[-1]:
            self.max.append(n)
        else:
            self.max.append(self.max[-1])
        self.main.append(n)


max = MaxStack()
max.push(3)
max.push(5)
max.push(2)

print(max.max)
print(max.main)
