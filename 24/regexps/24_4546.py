import re

f = open('../data_kompege/24_4546.txt').readline()

reg = '(A.A|C.C)*'
print(max(len(i.group(1)) // 3 for i in re.finditer(rf'(?=({reg}))', f)))