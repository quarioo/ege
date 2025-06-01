import math

x, y = 0, 0

for i in range(8):
    x, y = x + 30, y + 10
    x, y = x + 50, y - 30
    x, y = x - 40, y + 50

print(x, y)

print(math.dist((0 ,0), (x, y)))
