def div(x):
    r = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            r.add(i)
            r.add(x // i)

    return sorted(r)


for i in range(650_000, 650_000 + 10000):
    d = div(i)
    if len(d) == 6 and 1000 <= d[0] + d[-1] <= 9999:
        print(i, d[0] + d[-1])