from fnmatch import fnmatch


def div(x):
    r = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            r.add(i)
            r.add(x // i)
    return sorted(r)


for n in range(65001, 10 ** 10):
    if fnmatch(str(n), '6*97*5?'):
        d = [j for j in div(n) if j % 2 == 0]
        if len(d) >= 4:
            print(n, sum(d))
