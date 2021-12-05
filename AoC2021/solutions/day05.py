import re
from collections import defaultdict


with open("../inputs/05.txt") as f:
    lines = [[int(x) for x in re.split(" -> |,", line)] for line in f]

field = defaultdict(int)
for x1, y1, x2, y2 in lines:
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            field[x1, i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
            field[i, y1] += 1

part1 = sum(field[points] > 1 for points in field)
print(f'Day 5 part 1: {part1}')

for x1, y1, x2, y2 in lines:
    if x1 != x2 and y1 != y2:
        xs = range(x1, x2+1) if x1 < x2 else range(x1, x2-1, -1)
        ys = range(y1, y2+1) if y1 < y2 else range(y1, y2-1, -1)
        for x, y in zip(xs, ys):
            field[x, y] += 1

part2 = sum(field[points] > 1 for points in field)
print(f'Day 5 part 2: {part2}')
