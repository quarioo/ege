import sys

sys.setrecursionlimit(1000000)

def f(n):
    if n > 10000:
        return 42
    if n % 2 == 0 and n <= 10000:
        return 2 * n + f(n + 3) + f(n + 4) + f(n + 6)
    if n % 2 == 1 and n <= 10000:
        return -(n + f(n +1) + f(n + 3))

print(f(9996) - f(9994))