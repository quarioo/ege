from itertools import *

v = '234 157 147 138 268 58 23 456'.split()
e = 'dg bd be ed ga gf af fh eh bc ch'.split()

print(*range(1, 9))
for p in permutations('abcdefgh'):
    if all(str(p.index(a)+ 1) in v[p.index(b)] for a, b in e):
        print(*p)

print(4 + 7)