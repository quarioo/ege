# самый частый вариант задания - рекурсивная и динамическая реализация

def f(curr, end):
    if curr > end:
        return 0
    if curr == end:
        return 1
    return f(curr + 1, end) + f(curr * 2, end)


print(f(2, 8) * f(8, 20))


def f(curr, end):
    if curr > end or curr == 4:
        return 0
    if curr == end:
        return 1
    if curr < end:
        return f(curr + 1, end) + f(curr * 2, end)


print(f(2, 16))

dp = [0] * 1000
dp[2] = 1
for i in range(2, 8):
    if i + 1 <= 8: dp[i + 1] += dp[i]
    if i * 2 <= 8: dp[i * 2] += dp[i]

for i in range(8, 20):
    dp[i + 1] += dp[i]
    dp[i * 2] += dp[i]

print(dp[20])
