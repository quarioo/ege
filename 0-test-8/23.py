def f(s, e, t):
    if s > e:
        return 0
    if s == e:
        return (17 in t or 13 in t) and (not (17 in t and 13 in t))
    return f(s + 2, e, t + [s + 2]) + f(s + 3, e, t + [s + 3]) + f(s + 5, e, t + [s + 5])

print(f(5, 25, [5]))



