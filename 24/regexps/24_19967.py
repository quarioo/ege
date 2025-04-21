import re

f = open('../data_kompege/24_19967.txt').readline()

num = '([1-9][0-9]*|0)'
reg = rf'AFD({num}[*+])*{num}'
print(len(max([i.group(1) for i in re.finditer(rf'(?=({reg}))', f)], key=len)))