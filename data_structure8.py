from tkinter import N
from typing import Optional


def count(a_string: str) -> None:
    a_dict: dict[str, int] = {}
    for char in a_string:
        if char not in a_dict:
            a_dict[char] = 1
        else:
            a_dict[char] += 1
    print(a_dict)


count("takashi")


def two_sum(a_list: list[int], target: int) -> Optional[tuple[int, int]]:
    a_dict: dict[int, int] = {}
    for index, num in enumerate(a_list):
        rem = target - num
        if rem in a_dict:
            return index, a_dict[rem]
        else:
            a_dict[rem] = index
    return


def remove_duplicate(a_string: str) -> str:
    a_dict: dict[str, None] = {}
    a_list = a_string.rstrip(".").split()
    result = ""
    for char in a_list:
        if char not in a_dict:
            a_dict[char] = None
    for char in a_dict:
        result += " " + char
    return result + "."


if __name__ == "__main__":
    a_string = "I am a self-taught programmer looking for a job as a programmer."
    print(remove_duplicate(a_string))
