ans = set()

for k in range(1000):
    for n in range(1000):
        if 2*k + 3 * n == 1812:
            ans.add((n, k))

print(len(ans))
