import re

f = open('../data_kompege/24_19968.txt').readline()

num = r'([1-5][0-5]*|0)'
reg = rf'{num}([*+]{num})*'
print(len(max([i.group(1) for i in re.finditer(rf'(?=({reg}))', f)], key=len)))