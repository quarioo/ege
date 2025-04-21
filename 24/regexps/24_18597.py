import re

f = open('../data_kompege/24_18597.txt').readline()

num = '[1-9][0-9]{3}'
reg = rf'{num}(\.[0-9]*|)&{num}(\.[0-9]*|)'
print(len(max([i.group(1) for i in re.finditer(rf'(?=({reg}))', f)], key=len)))
