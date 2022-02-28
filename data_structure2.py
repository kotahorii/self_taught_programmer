list1 = [2, 43, 48, 62, 64, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
set1 = set(list1)
set2 = set(list2)

print(list(set1.intersection(set2)))

an_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def move_odd(a_list: list[int]) -> list[int]:
    odd_index = 0
    for index, n in enumerate(a_list):
        if n % 2 == 0:
            value = a_list[odd_index]
            a_list[odd_index] = n
            if odd_index != index:
                a_list[index] = value
            odd_index += 1
    return a_list


print(move_odd(an_array))
