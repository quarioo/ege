f = open('../data_kompege/24_21.txt').readline()

dp = [1] * len(f)
for i in range(1, len(f)):
    if f[i] != f[i - 1]:
        dp[i] = dp[i - 1] + 1

print(max(dp))
