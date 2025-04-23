import statistics
from math import dist
from turtle import *
from random import *

f = [list(map(float, i.split("\t"))) for i in open('27-57b.txt').readlines()]
# clusters = []

def mc(sp):
    cl = [sp]

    for cp in cl:
        for p in f:
            if dist(p, cp) < 1:
                cl.append(p)
                f.remove(p)

    return cl

cls = []
while f:
    cls.append(mc(f.pop()))

def draw():
    tracer(0)
    up()
    for cl in cls:
        c = random(), random(), random()
        for x, y in cl:
            goto(x * 20, y * 20)
            dot(3, c)

    update()
    exitonclick()

# draw()
def ce(cl):
    r = ([10000, 10000], 10000)
    for p in cl:
        s = sum(dist(p, i) for i in cl)
        if r[1] > s:
            r = (p, s)

    return r[0]

ces = [*zip(*[ce(i) for i in cls])]
print(statistics.mean(ces[0]) * 100000)
print(statistics.mean(ces[1]) * 100000)

