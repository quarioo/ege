import math
from turtle import *

k = 30

tracer(0)
up()

up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3)

goto(0,0)

rt(30)
fd(4 * k)
rt(330)

down()
fd(4 * k)
rt(90)
fd(7 * k)
rt(45)
fd(4 * math.sqrt(2) * k)
rt(135)
fd(11 * k)


up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3)

update()
exitonclick()