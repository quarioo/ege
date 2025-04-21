f = open('../data_kompege/24_2427.txt').readline()

dp = list(f)
for i in range(1, len(f)):
    if ord(f[i - 1]) > ord(f[i]):
        dp[i] = dp[i - 1] + dp[i]

print(max(dp, key=len))
