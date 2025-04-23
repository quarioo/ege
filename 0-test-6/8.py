import itertools

def prod(seq):
    r = 1
    for i in seq:
        r *= i
    return r

a = (itertools.product('ги', repeat=6))

ans = 0
d = {'г': 5, 'и': 4}
for p in a:
    if p[0] != 'и' and p[-1] != 'и':
        s = prod([d[i] for i in p])
        ans += s

print(ans)