import array
from typing import Any

arr = array.array("f", (1.0, 1.5, 2.0, 2.5))


def move_zeros(a_list: list[int]) -> list[int]:
    zero_index = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return a_list


a_list = [8, 0, 3, 0, 12]
move_zeros(a_list)
print(a_list)

movie_list = ["Interstellar", "Inception", "The Prestige", "Insomnia", "Batman Begins"]
ratings_list = [1, 10, 10, 8, 6]
print(list(zip(movie_list, ratings_list)))


def return_dups(an_iterable: Any) -> list[Any]:
    dups: list[Any] = []
    a_set: set[Any] = set()

    for item in an_iterable:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        if l1 == l2:
            dups.append(item)
    return dups


a_list = ["Susan Adams", "Kwame Goodall", "Jill Hampton", "Susan Adams"]

dups = return_dups(a_list)
print(dups)
