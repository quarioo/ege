def f(s, e):
    if s >= e:
        return s == e
    if s != 25:
        return f(s + 3, e) + f(s * 2, e) + f(s * 5, e)
    else: return 0


print(f(5, 115))