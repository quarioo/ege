def div(x):
    r = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            r.add(i)
            r.add(x // i)
    return sorted(r)


for i in range(154_026, 154_043 + 1):
    d = div(i)
    if len(d) == 4:
        print(*d[-2:])