# вариация где подходят только с предпоследней командой 2

def f(curr, end, comm):
    if curr > end:
        return 0
    if curr == end and comm[-2] == '2':
        return 1
    return f(curr + 1, end, comm+'1') + f(curr + 2, end, comm+'2')

print(f(3, 18, ''))