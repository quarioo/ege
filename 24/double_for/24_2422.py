from tkinter.font import names

f = open('../data_kompege/24_2422.txt').readline()

a = 0
for l in range(len(f)):
    for r in range(l + a, len(f)):
        s = f[l: r + 1]
        if all(s[i - 1] <= s[i] for i in range(1, len(s))):
            a = max(a, len(s))
        else:
            break

print(a)