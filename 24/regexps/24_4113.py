import re

f = open('../data_kompege/24_4113.txt').readline()

reg = r'(BB|DD)*'
print(max([len(i.group(1)) // 2 for i in re.finditer(rf'(?=({reg}))', f)]))