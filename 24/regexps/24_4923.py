import re

f = open('../data/24-196.txt').readline()

print(max(len(i.group())//2 for i in re.finditer(r'(ZX|ZY)+', f)))