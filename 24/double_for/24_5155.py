f = open('../data/24-204.txt').readline()

a = 0
for l in range(len(f)):
    for r in range(l + a, len(f)):
        s = f[l: r + 1]
        if len(s) % 2 == 0:
            if all(s[i] + s[i + 1] in ('AA', 'CC') for i in range(0, len(s), 2)):
                a = max(a, r + 1 - l)
            else:
                break

print(a // 2)