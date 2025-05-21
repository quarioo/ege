def t(x):
    r = ''
    while x > 0:
        r = f'{x % 7}' + r
        x //= 7
    return r

def f(n):
    x = t(n)
    if x.count('2') % 2 == 0:
        x = x + '555'
    else:
        x = '1' + x

    return int(x, 7)

for i in range(10_000_000):
    if f(i) < 3799:
        print(i)