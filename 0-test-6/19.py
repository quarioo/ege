def f(s, p):
    if s >= 229:
        return (p - 1) % 2
    if p == 0:
        return 0
    h = [
        f(s + 2, p - 1),
        f(s + 3, p - 1),
        f(s + 4, p - 1),
        f(s * 2, p - 1)
    ]
    return any(h) if (p - 1) % 2 == 0 else all(h)

print(min(s for s in range(1, 229) if not f(s, 1) and f(s, 2)))
print(*(s for s in range(1, 229) if not f(s, 1) and f(s, 3)))
print(min(s for s in range(1, 229) if not f(s, 2) and f(s, 4)))
