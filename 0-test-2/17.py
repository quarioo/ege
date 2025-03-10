# забыл abs при проверке на пятизначное и перепутал знак в условии
n = list(map(int, open('17_19249.txt')))


def f(i):
    return 99999 >= abs(i) >= 10000 and abs(i) % 100 == 43


a = list()
m = max([i for i in n if f(i)])

for i in range(len(n) - 2):
    t = [n[i], n[i + 1], n[i + 2]]
    s = sum(i * i for i in t)
    if any(f(i) for i in t) and m * m >= s:
        a.append(s)

print(len(a), min(a))
