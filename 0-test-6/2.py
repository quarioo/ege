from itertools import product, permutations


def f(a, b, c,d ):
    return ((a and b) <= c) and ((b and c) <= d)

for a in product([0, 1], repeat=6):
    t = [
        (a[0], 1, 1, 1),
        (a[1], 1, a[2], 1),
        (1, 1, 1, a[3]),
        (a[4], 1, 1, a[5])
    ]
    if len(t) == len(set(t)):
        for p in permutations('abcd'):
            if [f(**dict(zip(p, row))) for row in t] == [0, 0, 0, 0]:
                print(*p)