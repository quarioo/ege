f = open('../data/24-280.txt').readline()

l = 0
ans = 0
x_cnt = 0
y_cnt = 0

for r in range(len(f)):
    if f[r] == 'X': x_cnt += 1
    if f[r] == 'Y': y_cnt += 1
    while x_cnt > 1 or y_cnt > 1:
        if f[l] == 'X': x_cnt -= 1
        if f[l] == 'Y': y_cnt -= 1
        l += 1

    if x_cnt == y_cnt == 1: ans = max(ans, r - l + 1)

print(ans)