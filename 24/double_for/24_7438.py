f = open('../data/24-293.txt').readline()

a = 0
for l in range(len(f)):
    for r in range(l + a, len(f)):
        s = f[l: r + 1]
        c = s.count('D')
        if c == 100 and all(i not in s for i in '0123456789') and 'DS' not in s and 'SD' not in s:
            a = max(a, r + 1 - l)
        elif c > 100:
            break

print(a)