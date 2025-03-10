import sys
from functools import lru_cache

sys.setrecursionlimit(1000000)

@lru_cache()
def f(x, y, s):
    if (x + y) >= 231: return s % 2 == 0
    if s == 0: return 0
    h = [f(x + 4, y, s - 1), f(x * 3, y, s - 1), f(x, y + 4, s - 1), f(x, y * 3, s - 1)]

    return any(h) if (s - 1) % 2 == 0 else all(h)

print(19, [i for i in range(1, 218) if f(10, i, 2)])
print(20, [i for i in range(1, 218) if not f(10, i, 1) and f(10, i, 3)])
print(21, [i for i in range(1, 218) if not f(10, i, 2) and f(10, i, 4)])