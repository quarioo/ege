import re

f = open('../data/24-1.txt').readline()

print(min(int(i.group()) for i in re.finditer(r'[1-9][0-9]*', f) if int(i.group()) % 2 == 0))
