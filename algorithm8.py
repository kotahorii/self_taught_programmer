from operator import is_

print(2 | 3)


def is_even(n: int):
    return not n & 1


print(is_even(4))
