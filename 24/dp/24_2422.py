f = open('../data_kompege/24_2422.txt').readline()

dp = [1] * len(f)
for i in range(1, len(f)):
    if ord(f[i - 1]) <= ord(f[i]):
        dp[i] = dp[i - 1] + 1

print(max(dp))