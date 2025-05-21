f = open('../data/24-263.txt').readline()

a = 100_000
for l in range(len(f)):
    for r in range(l + a, l, -1):
        s = f[l:r + 1]
        if s.count('Z') >= 120:
            a = min(a, r + 1 - l)
        else:
            break
print(a)