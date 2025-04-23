from itertools import *
from random import random

s = "35 3457 1256 25 12347 3 25".split()
v = 'тп тс лп лс пс пр рс рм рк кс'.split()

print(*range(1, 9))
for p in permutations('тлпсрмк'):
    if all(str(p.index(a) + 1) in s[p.index(b)] for a, b in v):
        print(*p)