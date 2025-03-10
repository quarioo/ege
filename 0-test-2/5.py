# неправильно понял условие
def foo(x):
    r = list()
    while x > 0:
        r = [x % 3] + r
        x //= 3
    return r


def f(n):
    a = foo(n)
    if n % 3 == 0:
        a += [a[-2], a[-1]]
    else:
        a += foo(sum(a))
    return int(''.join(map(str, a)), 3)


print(f(11), f(12))

ans = float('inf')
for i in range(1, 1000000):
    i = f(i)
    if i % 2 == 0 and i > 220:
        ans = min(ans, i)

print(ans)