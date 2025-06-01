ans = 0
for line in open('9.txt'):
    line = list(map(int, line.split('\t')))
    if max(line) < sum(line) - max(line) and sum(i for i in line if i % 2 == 0) == sum(i for i in line if i % 2 == 1):
        ans += 1

print(ans)