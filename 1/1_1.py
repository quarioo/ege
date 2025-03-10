from itertools import *

v = '248 157 456 136 23 34 28 17'.split()
e = 'ch cf cg gd dh hb fa ba be ea'.split()

print(*range(8))
for p in permutations('abcdefgh'):
    if all(str(p.index(b) + 1) in v[p.index(a)] for a, b in e):
        print(*p)