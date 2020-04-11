import re
from z3 import Int, If, Optimize


def Abs(x):
    return If(x >= 0, x, -x)


def Dist(x, y, z, a, b, c):
    return Abs(x-a) + Abs(y-b) + Abs(z-c)


with open('../inputs/23.txt') as f:
    bots = [list(map(int, re.findall(r'-?\d+', l))) for l in f]
    mx, my, mz, mr = max(bots, key=lambda x: x[-1])

print('Day 23 part 1: ' + str(sum(abs(bx - mx) + abs(by - my) + abs(bz - mz) < mr for bx, by, bz, br in bots)))

X = x, y, z = Int('x'), Int('y'), Int('z')
cost = Int('cost')
constraint = x * 0
for *Y, r in bots:
    constraint += If(Dist(*X, *Y) <= r, 1, 0)

opt = Optimize()
opt.add(cost == constraint)
h1 = opt.maximize(cost)
h2 = opt.minimize(Dist(*(0, 0, 0), *X))
opt.check()
print('Day 23 part 2: ' + str(opt.lower(h2)))
