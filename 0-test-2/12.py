def f(s):
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)
    return s


for i in range(3, 10000):
    s = f('1' + i * '2')
    if sum(map(int, s)) == 15:
        print(i)
        break