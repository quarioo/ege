import re

f = open('../data_kompege/24_6734.txt').readline().split('.')

print(min([len(''.join(f[i:i + 6])) for i in range(len(f) - 6)]) + 7)