from fnmatch import *

for i in range(100110, 10 ** 8 + 1, 141):
    if fnmatch(str(i), '1234*7'):
        print(i, i // 141)