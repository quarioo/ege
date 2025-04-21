f = open('../data_kompege/24_13715.txt').readline()

l = 0
k = 0
ans = ''
for r in range(1, len(f)):
    if f[r - 1] + f[r] == 'AB':
        k += 1

    while k > 50:
        if f[l] + f[l + 1] == 'AB':
            k -= 1

        l += 1

    if k == 50:
        if len(ans) < len(f[l:r + 1]):
            ans = f[l:r + 1]

print(ans)