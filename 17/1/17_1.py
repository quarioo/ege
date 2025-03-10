n = list(map(int, open('17_2.txt')))

ans = []
for i in range(len(n) - 1):
    s = n[i] + n[i + 1]
    p = n[i] * n[i + 1]

    if s % 3 == 0 and s % 6 != 0 and abs(p) % 10 == 8:
        ans.append(s)

print(len(ans), max(ans))
