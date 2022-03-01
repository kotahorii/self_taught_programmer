from __future__ import annotations

import random
from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next: Node = None) -> None:
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

    def search(self, target: Any) -> bool:
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False

    def remove(self, target: Any):
        if self.head == target:
            self.head = self.head.next
            return
        current = self.head
        previous: Optional[Node] = None
        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next

    def reverse_list(self):
        current = self.head
        previous: Optional[Node] = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False

    def create_cycle(self):
        head = self.head
        current = self.head
        while current.next:
            current = current.next
        current.next = head


a_list = LinkedList()
for i in range(1, 101):
    a_list.append(i)


print(a_list.detect_cycle())
a_list.create_cycle()
print(a_list.detect_cycle())
