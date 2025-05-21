import string

f = open('../data/24-s2.txt').readline()

d = {i: 0 for i in string.printable}
a = 0
for i in range(1, len(f)):
    if f[i - 1] == 'X':
        d[f[i]] += 1

print(max(d.values()))
