n = list(map(int, open('17_3.txt')))

m = max(filter(lambda x: x % 19 == 0, n))
ans = []
for i in range(len(n) - 1):
    s = n[i] + n[i + 1]
    if n[i] > m or n[i + 1] > m:
        ans.append(s)

print(len(ans), min(ans))