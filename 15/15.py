def f(x, a):
    return (x % 12 != 0 or x % 18 == 0) <= (x % a != 0)

for a in range(1, 10000):
    if all(f(x, a) == 1 for x in range(1, 1000)):
        print(a)
        break