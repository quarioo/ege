def div(x):
    r = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            r.add(i)
            r.add(x // i)
    return sorted(r)

def is_prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

a = []
for i in range(158928, 345293 + 1):
    d = [j for j in div(i) if is_prime(j)]
    if len(d) == 3 and d[0] * d[1] * d[2]:
        a.append(i)

print(len(a), min(a))