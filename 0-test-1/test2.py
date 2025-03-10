import itertools
import statistics

ans = 0
for i in itertools.permutations(range(9), r=4):
    if statistics.mean(i[:2]) == statistics.mean(i[2:]) == 4.5:
        print(i)
        ans += 1


print(ans)