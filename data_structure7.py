from typing import Any


class Queue:
    def __init__(self) -> None:
        self.s1: list[Any] = []
        self.s2: list[Any] = []

    def enqueue(self, item: Any):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s2.append(item)
        self.s1 = self.s2[::-1]
        self.s2 = []
        print("s1:", self.s1, end=" ")
        print("s2:", self.s2)

    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Cannot pop from empty queue")
        return self.s1.pop()


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
for i in range(3):
    print(queue.dequeue())

l = [1, 2, 3]
a = l[:2]
a[0] = 2
print(a)
print(l)
