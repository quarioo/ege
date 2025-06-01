from itertools import *

def f(x, y, z, w):
    return (x <= (y and (not z))) or w


for a in product([0, 1], repeat=6):
    t = [
        (a[0], a[1], 1, 0),
        (0, a[2], a[3], 1),
        (1, a[4], 1, a[5])
    ]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in t] == [0,0,0]:
                print(p)