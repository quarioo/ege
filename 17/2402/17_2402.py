def f(x):
    res = []
    while x > 0:
        res = [x % 3] + res
        x //= 3
    return res[-1] == 2


n = list(map(int, open('17_2402.txt')))

ans = []
for i in range(len(n) - 2):
    p = [n[i], n[i + 1], n[i + 2]]
    if (f(n[i]) + f(n[i + 1]) + f(n[i + 2])) >= 1:
        ans.append(min(p))

print(len(ans), sum(ans))