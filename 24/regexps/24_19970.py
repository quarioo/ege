import re

f = open('../data_kompege/24_19970.txt').readline()

num = '([1-9][0-9]*[05]|0)'
reg = rf'{num}([*+]{num})*'
print(len(max([i.group(1) for i in re.finditer(rf'(?=({reg}))', f)], key=len)))