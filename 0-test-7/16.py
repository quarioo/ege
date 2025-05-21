import functools
import sys

sys.setrecursionlimit(100000000)


@functools.lru_cache()
def f(n):
    if n == 1:
        return 1
    return f(n - 1) - 2 * g(n - 1)


@functools.lru_cache()
def g(n):
    if n == 1:
        return 1
    return f(n - 1) + g(n - 1) + n


for i in range(1, 37):
    g(i)

print(sum(map(int, str(g(36)))))
