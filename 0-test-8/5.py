def f(n):
    x = str(n)
    t = [int(x[0]) * int(x[1]), int(x[2]) * int(x[3])]
    x = str(min(t)) + str(max(t))
    return int(x)


print(f(5431))
for i in range(1000, 10000):
    if f(i) == 1214:
        print(i)