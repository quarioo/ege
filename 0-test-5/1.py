import itertools

s = '3457 456 167 128 126 2358 138 467'.split()
v = 'kb kr bc rc rl kl la ac aq cq bp qp lp'.split()

print(*range(8))
for i in itertools.permutations('kbrcaqpl'):
    if all(str(i.index(a) + 1) in s[i.index(b)] for a, b in v):
        print(*i)