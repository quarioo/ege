f = [list(map(int, line.split('\t')))for line in open('9.txt')]

ans = 0
for line in f:
    if all(line.count(i) == 1 for i in line) and (max(line) + min(line)) * 2 <= sum(line) - max(line) - min(line):
        ans += 1

print(ans)