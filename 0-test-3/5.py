def f(x):
    x = str(x)
    s = sum(int(x[i]) for i in range(len(x)) if i % 2 == 0)
    return f'{sum(map(int, x)) - s}' + f'{s}'

for i in range(50000):
    if f(i) == '612':
        print(i)
        break

print(f(369))