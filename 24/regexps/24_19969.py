import re

f = open('../data_kompege/24_19969.txt').readline()

reg = r'[a-z]*@[a-z]*\.[a-z]*'
print(len(max([i.group(1) for i in re.finditer(rf'(?=({reg}))', f)], key=len)))