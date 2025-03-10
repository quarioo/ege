# интересная вариация с двоичной записью

from functools import lru_cache


# обычный способ
@lru_cache()
def f(curr, end):
    if len(curr) > len(end):
        return 0
    if curr == end:
        return 1
    return f(bin(int(curr, 2) + 1)[2:], end, ) + f(curr + '0', end) + f(curr + '1', end)


print(f('100', '11011010'))


# смотрим как каждая комманда изменяет десятичное число
@lru_cache()
def f(curr, end):
    if curr > end:
        return 0
    if curr == end:
        return 1
    return f(curr + 1, end, ) + f(curr * 2, end) + f(curr * 2 + 1, end)


print(f(4, 218))
