from itertools import *
from random import random

s = "".split()
v = ''.split()

print(*range(1, 9))
for p in permutations('тлпсрмк'):
    if all(str(p.index(a) + 1) in s[p.index(b)] for a, b in v):
        print(*p)