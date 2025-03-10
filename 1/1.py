from itertools import *

v = '256 134 267 27 16 135 34'.split()
e = 'af fe ec ab bd dg fb ed cg'.split()

print(*range(8))
for p in permutations('abcdefg'):
    if all(str(p.index(b) + 1) in v[p.index(a)] for a, b in e):
        print(*p)