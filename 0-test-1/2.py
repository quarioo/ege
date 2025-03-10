import itertools
from itertools import permutations


def f(a, b, c, d):
    return (a <= b) and (b <= c) and (c <= d)

for a in itertools.product([0, 1], repeat=2):
    t = [
        (0, a[0], 1, 0),
        (0, a[1], 1, 0),
        (0, 1, 1, 1)
    ]
    if len(t) == len(set(t)):
        for p in permutations('abcd'):
            if [f(**dict(zip(p, row))) for row in t] == [1, 1, 1]:
                print(p)