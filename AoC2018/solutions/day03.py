from re import findall
from collections import Counter


data = [map(int, findall(r'\d+', i)) for i in open('../inputs/03.txt').read().splitlines()]
d = {}
for l in data:
    for i in range(l[1], l[1] + l[3]):
        for j in range(l[2], l[2] + l[4]):
            d[(i, j)] = -1 if d.get((i, j)) else l[0]

count = Counter(d.values())
print("Day 3 part 1: " + str(count[-1]))
print("Day 3 part 2: " + str(next(i[0] for i in data if count[i[0]] == i[3] * i[4])))
