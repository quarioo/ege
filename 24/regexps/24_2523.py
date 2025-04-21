import re

f = open('../data/24-1.txt').readline()

for i in re.finditer(rf'[0-9]+', f):
    print(i.group())