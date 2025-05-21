f = list(map(int, open('17_8427.txt').readlines()))

m = min(i for i in f if 100 <= abs(i) <= 999 and abs(i) % 10 == 3)

ans = []
for i in range(1, len(f)):
    p = [f[i - 1], f[i]]
    if [1000 <= abs(j) <= 9999 for j in p].count(True) == 1 and (p[0] * p[0] + p[1] * p[1]) % m == 0:
        ans.append(p[0] * p[0] + p[1] * p[1])

print(len(ans), max(ans))