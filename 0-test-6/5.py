def f(n):
    ns = sorted(n)
    r = sorted([str(int(ns[0]) + int(ns[-1])), str(int(ns[1]) * int(ns[2]))], key=int)
    # print(ns, n, *[str(int(ns[0]) + int(ns[-1])), str(int(ns[1]) * int(ns[2]))])
    return int(''.join(r))

for i in range(1000, 9999):
    i = str(i)
    if len(i) == len(set(i)) and f(i) > 85:
        print(i)
        break

print(f('1088'))

# 8 8

