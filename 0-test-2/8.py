import itertools

a = [*itertools.product(sorted('январь'), repeat=5)]

for i in range(len(a) - 1, -1, -1):
    w = a[i]
    if w[0] != 'я' and w.count('ь') <= 1 and 'яя' not in ''.join(a[i]):
        print(i + 1, w)
        break