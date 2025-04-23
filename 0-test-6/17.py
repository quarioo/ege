f = [int(i) for i in open('17.txt').readlines()]

m = 132

ans = []
for i in range(len(f) - 1):
    if f[i] + f[i + 1] < m * m:
        ans.append(f[i] + f[i + 1])

print(len(ans), max(ans))