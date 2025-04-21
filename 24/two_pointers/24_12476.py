# на каждом шаге беру PROREERPRGGGGR
#                     l r
f = open('../data_kompege/24_12476.txt').readline()

l = 0
ro = 0
oro = ror = 0
ans = 0
for r in range(2, len(f)):
    if f[r - 2:r + 1] == 'ROR':
        ror += 1
    if f[r - 2:r + 1] == 'ORO':
        oro += 1
    if f[r - 1:r + 1] == 'RO':
        ro += 1

    while oro != 0 or ror != 0 or ro > 21:
        if f[l:l + 3] == 'ROR':
            ror -= 1
        if f[l:l + 3] == 'ORO':
            oro -= 1
        if f[l:l + 2] == 'RO':
            ro -= 1
        l += 1

    if ro == 21:
        ans = max(ans, r - l + 1)

print(ans)
