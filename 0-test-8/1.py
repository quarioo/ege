from itertools import *

s = '267 1345 24 236 27 14 15'.split()
v = 'аб бв аг бд ве гд де гж жд'.split()

print(*range(1, 9))
for p in permutations('абвгедж'):
    if all(str(p.index(a) + 1) in s[p.index(b)] for a, b in v):
        print(*p)