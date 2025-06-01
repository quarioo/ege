f = sorted(map(int, open('26.txt').readlines()))

ans = []
for k in range(len(f)):
    for l in range(k + 1, len(f)):
        for m in range(l + 1, len(f)):
            if f[m] < f[k] + f[l]:
                ans.append(f[k] + f[l] + f[m])
            else:
                break

print(len(ans), max(ans))
