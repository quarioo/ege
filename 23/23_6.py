# нужно найти сколько программ из 6 команд существует которые идут от 1 к 20

def f(curr, end, comm):
    if curr > end:
        return 0
    if curr == end and comm == 6:
        return 1
    return f(curr + 1, end, comm + 1) + f(curr + 2, end, comm + 1) + f(curr * 2, end, comm + 1)


print(f(1, 20, 0))
