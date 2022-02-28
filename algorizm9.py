# def gcf(i1: int, i2: int) -> int:
#     if i1 < 0 or i2 < 0:
#         raise ValueError("Numbers must be positive")
#     if i1 == 0:
#         return i2
#     if i2 == 0:
#         return i1

#     if i1 > i2:
#         bigger = i1
#     else:
#         bigger = i2
#     for i in range(bigger // 2 + 1, 0, -1):
#         if i1 % i == 0 and i2 % i == 0:
#             return i
#     raise ValueError("Numbers must be positive")


import math


def gcf(x: int, y: int) -> int:
    if y == 0:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


print(gcf(20, 12))


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(n: int) -> list[int]:
    return [i for i in range(2, n) if is_prime(i)]


print(find_primes(100))
