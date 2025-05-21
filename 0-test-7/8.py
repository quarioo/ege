from itertools import product


def t(x):
    r = ''
    while x > 0:
        r = f'{x % 7}' + r
        x //= 7
    return r


ans = 0
for a in product(range(7), repeat=5):
    if a[0] != 0 and a.count(6) == 1:
        ch = sum(i for i in a if i % 2 == 0)
        nch = sum(i for i in a if i % 2 == 1)
        if ch < nch:
            ans += 1

print(ans)