f = open('26data/26-56.txt')
v, k, n = map(int, f.readline().split())
a = [v] * k

ans = []
s = 0
for l in sorted(map(int, f.readlines()), reverse=True):
    for i in range(s, s + k):
        if a[i % k] - l >= 0:
            a[i % k] -= l
            s = i + 1
            break
    else:
        ans.append(l)

print(sum(ans), len(ans))