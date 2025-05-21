f = open('../data/24-263.txt').readline()

a = 0
for l in range(len(f)):
    for r in range(l + a, len(f)):
        s = f[l:r]
        if s.count('Y') <= 150:
            a = max(a, len(s))
        else:
            break

print(a)