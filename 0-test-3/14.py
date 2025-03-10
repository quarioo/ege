def f(x):
    r = []
    while x > 0:
        r = [x % 6] + r
        x //= 6
    return r


print(f(36 ** 7 + 6 ** 30 - 12).count(5))