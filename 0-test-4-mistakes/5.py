def ns(x):
    r = ''
    while x > 0:
        r = f'{x % 3}' + r
        x //= 3

    return r

def f(x):
    n = ns(x)
    s = sum(map(int, n))
    if s % 3 == 0:
        n = '112' + n[2:]
    else:
        n = n + ns(s)
    return int(n, 3)


a = [f(i) for i in range(0, 10000)]
print(max(i for i in a if i < 679 and i % 2 == 0))
