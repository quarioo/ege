import re

f = open('../data_kompege/24_5171.txt').readline()

reg = r'(CA)*(CA|C)'
print(len(max([i.group(1) for i in re.finditer(rf'(?=({reg}))', f)], key=len)))