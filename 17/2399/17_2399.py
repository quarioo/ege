n = list(map(int, open('17_2399.txt')))
m = sum(sum(map(int, str(abs(i)))) for i in n if i % 35 == 0)
ans = []

for i in range(len(n) - 1):
    s = n[i] + n[i + 1]
    if ((n[i] > m and n[i + 1] <= m and abs(n[i + 1]) % (16 * 16) == int('ef', 16)) or
            (n[i + 1] > m and n[i] <= m and abs(n[i]) % (16 * 16) == int('ef', 16))):
        ans.append(s)

print(len(ans), min(ans))