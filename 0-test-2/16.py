# dp = [0] * 20000
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 4
# dp[5] = 5
#
# for i in range(5,13767):
#     dp[i] = 2 * i * dp[i - 4]
#
# print(dp[:10])
# print((dp[13766] - 9.txt * dp[13762]) / dp[13758])

import functools
import sys

# sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def f(x):
    if x < 5:
        return x
    if x >= 5:
        return 2 * x * f(x - 4)

for i in range(14000): f(i)
print((f(13766) - 9 * f(13762)) / f(13758))