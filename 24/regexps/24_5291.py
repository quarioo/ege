import re

f = open('../data/24-215.txt').readline()

print(max(len(i.group(1)) // 3 for i in re.finditer(r'(?=(([0-9][A-Z][0-9])+))', f)))