from random import *
from math import *
from turtle import *


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


def mc_a():
    for i in open('27-21a.txt'):
        x, y = map(float, i.split('\t'))
        if x < 5 and y < 5:
            cls[0].append((x, y))
        if x >= 5:
            cls[1].append((x, y))


# draw()
def solve_a(cl1, cl2):
    dmin = 1000
    dmax = 0
    for p1 in cl1:
        for p2 in cl2:
            dmin = min(dmin, dist(p1, p2))
            dmax = max(dmax, dist(p1, p2))

    return dmin, dmax


cls = [[], []]
mc_a()

dmn, dmx = solve_a(cls[0], cls[1])
print(int(dmn * 10_000), int(dmx * 10_000))


def mc_b():
    for i in open('27-21b.txt').readlines():
        x, y = map(float, i.split('\t'))

        if 8.2 > y > 5.9 and x < 6:
            cls[0].append((x, y))
        elif 7.5 < x < 11.5:
            cls[1].append((x, y))
        elif 5.5 > y > 1.5:
            cls[2].append((x, y))


def solve_b():
    ans = [solve_a(cls[0], cls[1]), solve_a(cls[0], cls[2]), solve_a(cls[2], cls[1])]
    return list(zip(*ans))


cls = [[], [], []]
mc_b()
a = solve_b()
dmx, dmn = min(a[0]), max(a[1])

print(int(dmx * 10_000), int(dmn * 10_000))
