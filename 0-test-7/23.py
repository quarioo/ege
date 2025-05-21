import math


def f(s, e):
    if s < e:
        return 0
    elif s == e:
        return 1
    return f(s - 3, e) + f(math.ceil(s / 2), e)

print(f(108, 42) * f(42, 12))