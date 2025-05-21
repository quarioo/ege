def f(x):
    return ((x % 4 != 3) or (x % 6 != 1)) <= (x % 36 != A)


for A in range(10000):
    if all(f(x) for x in range(100000000)):
        print(A)
        break