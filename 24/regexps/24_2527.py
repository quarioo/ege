import re

f = open('../data/24-1.txt').readline()

print(max(int(i.group()[1:-1]) for i in re.finditer(r'[^0-9][2468][02468]+[^0-9]', f)))