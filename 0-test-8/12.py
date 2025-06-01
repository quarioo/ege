def f(s):
    while '888' in s or '2222' in s:
        if '2222' in s:
            s = s.replace('2222', '88', 1)
        else:
            s = s.replace('888', '22', 1)
    return s


print(f('8' * 120))