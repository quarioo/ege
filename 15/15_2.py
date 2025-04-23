def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = s <= x <= e
    return (not A) <= (B == C)

d = [j for i in (36, 60, 75, 110) for j in (i - 0.25, i, i + 0.25)]

a = list()
for s in d:
    for e in d:
        if s <= e and all(f(x) for x in d):
            a.append(e - s)

print(min(a))