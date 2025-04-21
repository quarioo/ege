import re

f = open('../data/24-310.txt').readline()

num = rf'([1-2][0-2]*|0)'
reg = rf'{num}([+*]{num})*'


m = max([i.group(1) for i in re.finditer(rf'(?=({reg}))', f)], key=len)

print(len(m), m)
