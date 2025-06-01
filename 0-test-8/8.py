import itertools
from itertools import repeat

ans = 0
for i in itertools.product(range(15), repeat=5):
    if i[0] != 0 and i.count(8) == 1 and len([j for j in i if j > 9]) >= 2:
        ans += 1

print(ans)