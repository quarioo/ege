import statistics

n = list(map(int, open('17_2.txt')))

ans = []
for i in range(len(n) - 2):
    # s = n[i] + n[i + 1] + n[i + 2]
    t = n[i], n[i + 1], n[i + 2]
    if any(i % 12 == 0 for i in t) and all(i % 3 == 0 for i in t):
        ans.append(statistics.mean(t))

print(len(ans), min(ans))