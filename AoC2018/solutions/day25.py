with open('../inputs/25.txt') as f:
    points = [tuple(map(int, l.split(','))) for l in f]

manhattan = lambda a, b: sum(abs(a[i] - b[i]) for i in range(len(a)))
groups = []
for p in points:
    new, old = [p], []
    for i in range(len(groups)):
        if min(manhattan(p, point) for point in groups[i]) <= 3:
            new += groups[i]
        else:
            old.append(groups[i])
    groups = old + [new]

print('Day 25 part 1: ' + str(len(groups)))
