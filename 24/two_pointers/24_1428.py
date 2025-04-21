import re

f = open('../data_kompege/24_1428.txt').readline()

l = 0
a = 0
for r in range(len(f)):
    if f[r - 1: r + 1] in ('XY', "XZ"):
        l = r

    a = max(a, r - l + 1)

print(a)

dp = [0] * len(f)
for i in range(1, len(f)):
    if f[i - 1: i + 1] not in ('XY', 'XZ'):
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = 1

print(max(dp))
