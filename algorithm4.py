import time
from bisect import bisect_left

sorted_fruits = ["apple", "banana", "orange", "plum"]
start = time.time()
print(bisect_left(sorted_fruits, "banana"))
end = time.time()
print(end - start)


def binary_search(an_iterable: list[str], target: str) -> bool:
    index = bisect_left(an_iterable, target)
    return index <= len(an_iterable) and an_iterable[index] == target


print(binary_search(sorted_fruits, "kiwi"))
