import itertools
from itertools import permutations


def f(x, y, z):
    return (x == y) or ((z or y) <= x)

for a in itertools.product([0, 1], repeat=3):
    t = [
        (a[0], 1, a[1]),
        (a[2], 1, 1),
    ]
    if len(t) == len(set(t)):
        for p in permutations('xyz'):
            if [f(**dict(zip(p, row))) for row in t] == [0, 0]:
                print(p)