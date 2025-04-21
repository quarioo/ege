f = open('../data_kompege/24_11954.txt').readline()

l = 0
x = 0
ans = float('inf')
for r in range(len(f)):
    if f[r] == 'X':
        x += 1
    if f[r] == 'Y':
        l = r + 1
        x = 0

    while x >= 500:
        if x == 500:
            ans = min(ans, r - l + 1)
        if f[l] == 'X':
            x -= 1
        l += 1

print(ans)