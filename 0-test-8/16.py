d = dict()

for n in range(10001):
    if n <= 3:
        d[n] = n
    elif n % 2 == 1:
        d[n] = 2 * n + d[n - 2]
    elif n % 2 == 0:
        d[n] = n * n + d[n - 1]

print(d[10_000] - d[9_995])
