f = open('../data/24-263.txt').readline()

l = 0
ans = float('inf')
c = 0

for r in range(len(f)):
    if f[r] == 'Z': c += 1
    while c > 120:
        if f[l] == 'Z': c -= 1
        l += 1
    ans = min(ans, r - l + 1)

print(ans)