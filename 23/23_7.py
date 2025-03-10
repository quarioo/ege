# за какое минимальное кол-во ходов можно дойти от 1 к 227

from functools import *


@lru_cache(None)
def f(curr, end, comm):
    if curr > end:
        return 10 ** 8
    if curr == end:
        return comm
    return min(f(curr + 1, end, comm + 1), f(curr + 5, end, comm + 1), f(curr * 3, end, comm + 1))


print(f(1, 227, 0))
