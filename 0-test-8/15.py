def f(x):
    return ((x & 17 != 0) <= ((x & A != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & A != 0) and (x & 58 == 0))


for A in range(1, 10_000_000):
    if all(not f(x) for x in range(10000000)):
        print(A)

# A = 54
# print(all(not f(x) for x in range(100000000)))