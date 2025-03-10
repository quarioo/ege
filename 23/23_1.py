# вариация, где надо обязательно пройти через два числа

def f(curr, end):
    if curr > end:
        return 0
    if curr == end:
        return 1
    return f(curr * 2, end) + f(curr + 1, end) + f(curr + 3, end)


print(f(3, 10) * f(10, 20) * f(20, 30))
