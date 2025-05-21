from itertools import *

def f(x, y, z, w):
    return (w or x or (not z) or y) and (w or x or (not z) or (not y)) and (w or (not x) or (not y) or (not z))

# for a in product([0, 1], repeat=6):
#     t = [
#         (a[0], ),
#
#     ]
# for p in permutations('xzyw'):

for w, x, y, z in product([0, 1], repeat=4):
    if not f(x, y, z, w):
        print(w, y, z, x, int(f(x, y, z, w)))

#
# 0 0 1 0 0
# 0 1 1 0 0
# 1 1 1 0 0
