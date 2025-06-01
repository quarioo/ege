from fnmatch import fnmatch

for i in range(13, 10**9, 13):
    i = str(i)
    if fnmatch(i, '24*68?35') and i[-3] in ('3', '9') and all(int(j) % 2 == 0 for j in i[2:-5]):
        print(i, int(i) // 13)