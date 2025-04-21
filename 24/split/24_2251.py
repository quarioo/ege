import re

f = open('../data_kompege/24_2251.txt').readline().split('D')

print(max(len(f[i] + f[i + 1] + f[i + 2]) for i in range(len(f) - 2)) + 2)