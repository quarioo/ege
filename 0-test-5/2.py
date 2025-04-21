from itertools import product, repeat, permutations


def f(x, y, z, w):
    return ((((((w and x) == x) or 1) <= z) or (not x)) and y)

for a in product([0, 1], repeat=4):
    t = [
        (a[0], a[1], 1, 0),
        (1, a[2], 1, 0),
        (a[3], 0, 0, 1)
    ]
    if len(t) == len(set(t)):
        for i in permutations('xyzw'):
            if [f(**dict(zip(i, row))) for row in t] == [1, 1, 1]:
                print(*i)