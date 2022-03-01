from typing import Any

# class Stack:
#     def __init__(self) -> None:
#         self.items: list[Any] = []

#     def push(self, data: Any) -> None:
#         self.items.append(data)

#     def pop(self) -> Any:
#         return self.items.pop()

#     def size(self) -> int:
#         return len(self.items)

#     def is_empty(self) -> bool:
#         return len(self.items) == 0

#     def peek(self) -> Any:
#         return self.items[-1]


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node = None


class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, data: Any) -> None:
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self) -> Node:
        if self.head is None:
            raise IndexError("pop from empty stack")
        poppednode = self.head
        self.head = self.head.next
        return poppednode.data


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

for _ in range(3):
    print(stack.pop())
