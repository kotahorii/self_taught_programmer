from __future__ import annotations

from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next: Optional[Node] = None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        return ""

    def append(self, data: Any) -> None:
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)


a_list = LinkedList()
a_list.append("Tuesday")
a_list.append("Wednesday")
print(a_list)
