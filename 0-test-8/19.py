def f(s, p):
    if s == 42:
        return p % 2 == 0
    if s > 42:
        return (p - 1) % 2 == 0
    if p <= 0:
        return 0

    h = [
        f(s + 1, p - 1),
        f(s + 3, p - 1),
        f(s + 7, p - 1)
    ]

    return any(h) if (p - 1) % 2 == 0 else all(h)


print([s for s in range(0, 42) if f(s, 2)])
print([s for s in range(0, 42) if not f(s, 1) and f(s, 3)])
print([s for s in range(0, 42) if not f(s, 2) and f(s, 4)])
