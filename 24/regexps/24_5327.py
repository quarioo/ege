import re

f = open('../data/24-212.txt').readline()

print(f[:100])
print(max(len(i.group()) // 2 for i in re.finditer(r'([BCD][AO])+', f)))