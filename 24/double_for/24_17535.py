f = open('../data_kompege/24_17535.txt').readline()

a = 0
for l in range(len(f)):
    for r in range(l + a, len(f)):
        s = f[l: r + 1]
        k = s.count('CD')
        if k == 160:
            a = max(a, r - l + 1)
        elif k > 160:
            break
print(a)