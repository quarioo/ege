f = open('../data_kompege/24_21.txt').readline()

a = 0
for l in range(len(f)):
    for r in range(l + a, len(f)):
        s = f[l: r + 1]
        if all(s[i] != s[i +1 ] for i in range(r - l)):
            a = max(a, r + 1 - l)
        else:
            break

print(a)