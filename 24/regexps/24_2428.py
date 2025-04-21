import re

f = open('../data_kompege/24_2428.txt').readline()

reg = r'(XYZ|XY|Z)(XYZ)*(XYZ|XY|Z)'
print(len(max([i.group(1) for i in re.finditer(rf'(?=({reg}))', f)], key=len)))