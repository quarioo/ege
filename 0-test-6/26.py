from datetime import datetime

f = list(map(lambda x: x.split(), open('26.txt').readlines()))
f = list(map(lambda x: [datetime.fromisoformat(x[0])] + x[1:], f))

f = sorted(f, key=lambda x: x[0])
d = dict()

print(f[:10])
for i in f:
    if i[1] in d:
        d[i[1]].append([i[2]])
        if len(d[i[1]]) == 14:
            print(i[1])
    else:
        d[i[1]] = []

