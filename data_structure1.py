import array

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
