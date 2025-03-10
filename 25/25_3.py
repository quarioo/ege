def div(x):
    r = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            r.add(i)
            r.add(x // i)
    return sorted(r)


def is_prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


for n in range(500_000, 499_500, -1):
    d = [i for i in div(n) if is_prime(i)]
    if len(d) > 1 and sum(d) % 10 == 0:
        print(n, sum(d))