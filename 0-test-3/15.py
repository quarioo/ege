def f(x, y, A):
    return (x + 2 * y > 16) or (x + y <= A)


for A in range(0, 100000):
    if all(f(x, y, A) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break