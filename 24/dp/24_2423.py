f = (open('../data_kompege/24_2423.txt').readline()).rstrip('\n')

dp = [0] * len(f)
for i in range(1, len(f)):
    if int(f[i]) > int(f[i - 1]):
        dp[i] = dp[i - 1] + 1

print(max(dp))