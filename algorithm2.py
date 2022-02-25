# def factorial(n: int) -> int:
#     the_product = 1
#     while n > 0:
#         the_product *= n
#         n -= 1
#     return the_product


# print(factorial(5))


def factorial_v2(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial_v2(n - 1)


# print(factorial_v2(5))


def print_1_to_n(n: int) -> None:
    if n == 0:
        return
    print(n)
    return print_1_to_n(n - 1)


print_1_to_n(10)
