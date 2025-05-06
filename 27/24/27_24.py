import statistics
from statistics import *
from turtle import *
from random import *


def mc_a():
    for i in open('27-24a.txt'):
        x, y = map(float, i.split())
        if x < -4:
            cls[0].append((x, y))
        else:
            cls[1].append((x, y))


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


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return abs(x2 - x1) + abs(y2 - y1)


def ce(cl):
    ans = [[0, 0], 1000000]

    for p in cl:
        m = sum(dist(p, cp) for cp in cl)
        if ans[1] > m:
            ans = [p, m]

    return ans[0]


cls = [[], []]
mc_a()
# draw()
ces = list(zip(*[ce(cls[0]), ce(cls[1])]))
print(int(mean(ces[0]) * 10_000), int(mean(ces[1]) * 10_000))


def mc_b():
    for i in open('27-24b.txt'):
        x, y = map(float, i.split())
        if y > -2:
            cls[0].append((x, y))
        elif x < -2.5:
            cls[1].append((x, y))
        else:
            cls[2].append((x, y))


cls = [[], [], []]
mc_b()

ces = list(zip(*[ce(cls[0]), ce(cls[1]), ce(cls[2])]))
print(int(mean(ces[0]) * 10_000), int(mean(ces[1]) * 10_000))