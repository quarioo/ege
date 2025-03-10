# количество результатов за x ходов
ans = set()

def f(curr, comm):
    if comm > 5:
        return
    if comm == 4:
        ans.add(curr)
        return
    f(curr + 1, comm + 1)
    f(curr + 5, comm + 1)
    f(curr * 3, comm + 1)

f(1, 0)
print(len(ans))