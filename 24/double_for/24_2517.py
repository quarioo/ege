f = open('../data/k7data/k7a-3.txt').readline()

a = 0
for l in range(len(f)):
    for r in range(l + a, len(f)):
        s = f[l:r + 1]
        if 'C' not in s and 'D' not in s:
            a = max(a, r - l + 1)
        else:
            break

print(a)
