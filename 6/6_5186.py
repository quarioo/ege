from turtle import *

screensize(10000, 10000)
lt(90)
pd()
k = 20

for i in range(3):
    fd(10 * k)
    rt(120)

pu()
fd(10 * k)
rt(90)
fd(3 * k)

pd()
for i in range(4):
    fd(10 * k)
    rt(90)

exitonclick()