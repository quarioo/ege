import re

f = open('../data_kompege/24_2425.txt').readline()
reg = '(DBAC)*(DBAC|DBA|DB|D)'
print(len(max([i.group(1) for i in re.finditer(rf'(?=({reg}))', f)], key=len)))