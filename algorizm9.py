def gcf(i1: int, i2: int) -> int:
    if i1 == 0:
        return i2
    if i2 == 0:
        return i1

    if i1 > i2:
        bigger = i1
    else:
        bigger = i2
    for i in range(bigger // 2 + 1, 0, -1):
        if i1 % i == 0 and i2 % i == 0:
            return i


print(gcf(9, 6))
