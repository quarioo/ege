def f(x):
    P = 117 <= x <= 158
    Q = 130 <= x <= 180
    A = s <= x <= e
    return P <= (((not A) and Q) <= (not P))

d = [j for i in (117, 130, 158, 180) for j in (i, i - 0.1, i + 0.1)]

a = []
for s in d:
    for e in d:
        if s <= e and all(f(x) for x in d):
            a.append(e - s)

print(round(min(a)))
