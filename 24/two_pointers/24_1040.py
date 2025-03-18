import re
import string

f = open('../kompege_data/24_1040.txt').readline()

l = 0
a = 0
for r in range(len(f)):
    if f[r].isalpha():
        l = r + 1

    a = max(a, r - l + 1)

print(a)

dp = [0] * len(f)
for i in range(1, len(f)):
    if f[i].isdigit():
        dp[i] = dp[i - 1] + 1

print(max(dp))

print(max(map(len, re.findall(r'[0-9]*', f))))

for i in string.ascii_letters:
    f = f.replace(i, ' ')

print(max(map(len, f.split())))