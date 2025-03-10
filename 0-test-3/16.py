def f(x):
    if x == 1 or x == 2:
        return x
    return 3 * f(x - 1) - f(x - 2)

print(f(8))