def f(x, y):
    return (3 * x + y > a) and (y < x) and (x < 30)

for a in range(0, 1000):
    if all(f(x, y) == 0 for x in range(0, 2000) for y in range(0, 2000)):
        print(a)
        break