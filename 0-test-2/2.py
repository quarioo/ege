from itertools import *


def f(x, y, z, w):
    A = ((not x) or y) and (not w)
    B = z and (not (y and w))
    return (not A) or (not B)


for a in product([0, 1], repeat=7):
    t = [
        (0, a[0], a[1], 1),
        (a[2], 1, a[3], a[4]),
        (1, 0, a[5], a[6])
    ]
    if len(set(t)) == len(t):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in t] == [0, 0, 0]:
                print(*p)
