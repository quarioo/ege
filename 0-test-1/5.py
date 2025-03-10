def g(x):
    a = ''

    while x > 0:
        a = str(x % 5) + a
        x //= 5

    return a

def f(n):
    a = g(n)
    if n % 25 == 0:
        a = a[-3:] + a
    else:
        a = a + g(n % 25)

    return int(a, 5)

for i in range(1, 10000000):
    if f(i) > 10000:
        print(i)
        break
