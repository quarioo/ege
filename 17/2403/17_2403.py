n = list(map(int, open('17_2403.txt')))

ans = []
for i in range(len(n) - 1):
    if ((n[i] % 9 == 0 and n[i + 1] % 9 != 0 and n[i + 1] % 8 == 3) or
            (n[i + 1] % 9 == 0 and n[i] % 9 != 0 and n[i] % 8 == 3)):
        ans.append(max((n[i], n[i + 1])))

print(len(ans), max(ans))
