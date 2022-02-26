import time


def linear_search(a_list: list[int], n: int) -> bool:
    for i in a_list:
        if i == n:
            return True
    return False


a_list = [1, 8, 32, 91, 5, 15, 9, 100, 3]
start = time.time()
print(linear_search(a_list, 3))
end = time.time()

print(end - start)


def binary_search(a_list: list[int], n: int) -> bool:
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


a_list = sorted(a_list)
start = time.time()
print(binary_search(a_list, 100))
end = time.time()
print(end - start)
