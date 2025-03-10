import statistics
from itertools import *

f = [list(map(int, i.split('\t'))) for i in open('9.txt').readlines()]

for j in range(len(f) - 1, -1, -1):
    s = f[j]
    c = [s.count(i) for i in s]
    if (c.count(3) == 6 and c.count(1) == 1 and
            statistics.mean(compress(s, filter(lambda x: x == 3, c))) < s[c.index(1)]):
        print(j + 1, s)
        break
