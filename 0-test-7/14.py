def t(x):
    return sum(111 ** (len(x) - 1 - i) * x[i] for i in range(len(x)))

def t2(x):
    return sum(211 ** (len(x) - 1 - i) * x[i] for i in range(len(x)))

for x in range(111):
    s = t([x, 3, 2, 1]) + t2([1, 7, x, 4])
    if s % 111 == 0:
        print(s // 111)