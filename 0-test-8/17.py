n = list(map(int, open('17.txt').readlines()))

mi = min(n)
ans = []
for i in range(1, len(n)):
    t = [n[i - 1], n[i]]
    if t[0] % 117 == mi or t[1] % 117 == mi:
        ans.append(sum(t))

print(len(ans), max(ans))
