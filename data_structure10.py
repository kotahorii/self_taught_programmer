from ctypes import Union
from heapq import heapify, heappop, heappush
from typing import Any

# heappush(a_list, "Z")
# print(a_list)
# heappop(a_list)
# print("After popping")
# print(a_list)


def find_min_cost(ropes: list[int]):
    heapify(ropes)
    print(ropes)
    cost = 0
    while len(ropes) > 1:
        sum = heappop(ropes) + heappop(ropes)
        heappush(ropes, sum)
        cost += sum
    return cost


a_list = ["R", "C", "T", "H", "E", "D", "L"]
heapify(a_list)


def is_min_heap(a_list: list[Any]) -> bool:
    i = 0
    while i < len(a_list):
        if 2 * i + 1 > len(a_list) or 2 * i + 2 > len(a_list):
            return True
        if a_list[i] > a_list[2 * i + 1]:
            return False
        if a_list[i] > a_list[2 * i + 2]:
            return False
        i += 1
    return False


print(is_min_heap(a_list))
