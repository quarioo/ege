def div(x):
    r = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i ==0 :
            r.add(i)
            r.add(x//i)

    return sorted(r) or [0]


for i in range(452_022, 452_021 + 100):
    d = div(i)
    M = max(d) + min(d)
    if M % 7 == 3:
        print(i, M)