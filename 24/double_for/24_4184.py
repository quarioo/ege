f = open('../data/24-173.txt').readline()

a = 0
for l in range(len(f)):
    for r in range(l + a, len(f)):
        s = f[l: r + 1]
        if all(s[i: i + 3] != s[i + 3: i + 6]  for i in range(len(s) - 5)):
            a = max(a, len(s))
        else:
            break

print(a)