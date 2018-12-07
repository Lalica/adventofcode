def mandis(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


data = [map(int, i.split(", ")) for i in open('../inputs/06.txt').read().strip().splitlines()]
d, maxic = {}, max(max(k[0] for k in data), max(k[1] for k in data))

for x in range(maxic):
    for y in range(maxic):
        mini = min(mandis(x, i[0], y, i[1]) for i in data)
        for n, i in enumerate(data):
            if mandis(x, i[0], y, i[1]) != mini:
                continue
            if d.get((x, y), None):
                d[(x, y)] = -1
                break
            d[(x, y)] = n
            #tmp = list(n for n, i in enumerate(data) if mandis(x, i[0], y, i[1]) == mini)
            # tmp = list(i for i in range(len(data)) if mandis(x, data[i][0], y, data[i][1]) == mini)

bad = set(d[x, y] for e in range(maxic) for x, y in [(e, 0), (e, maxic - 1), (0, e), (maxic - 1, e)])
print("Day 6 part 1: " + str(max(d.values().count(i) for i in range(len(data)) if i not in bad)))

size = 0
for x in range(maxic):
    for y in range(maxic):
        sumi = sum(mandis(x, i[0], y, i[1]) for i in data)
        if sumi < 10000:
            size += 1
print("Day 6 part 2: " + str(size))
