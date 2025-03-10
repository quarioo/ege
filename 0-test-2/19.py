def f(c, p):
    if c >= 132:
        return p % 2 == 0
    if p == 0:
        return 0
    h = [
        f(c + 3, p - 1),
        f(c + 6, p - 1),
        f(c * 3, p - 1)
    ]
    return any(h) if (p - 1) % 2 == 0 else all(h)


print(min(i for i in range(1, 132) if not f(i, 1) and f(i, 2)))
print([i for i in range(1, 132) if not f(i, 1) and f(i, 3)])
print(min(i for i in range(1, 132) if not f(i, 2) and f(i, 4)))
