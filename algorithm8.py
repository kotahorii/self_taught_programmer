from operator import is_

print(2 | 3)


def is_even(n: int):
    return not n & 1


print(is_even(4))


def is_power(n: int) -> bool:
    return n & n - 1 == 0


print(is_power(8))


def fizzbuzz(n: int) -> None:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


fizzbuzz(100)
