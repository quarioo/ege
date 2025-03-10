from itertools import *

v = '248 13 268 17 678 358 45 1356'.split()
e = 'аб аг ав бг ве ге бд гд дк кл ел'.split()

print(*range(1, 9))
for p in permutations('абвгдекл'):
    if all(str(p.index(a) + 1) in v[p.index(b)] for a, b in e):
        print(*p)
