from collections import defaultdict


heightmap = defaultdict(lambda: 9)
with open("../inputs/09.txt") as f:
    for i, line in enumerate(f):
        for j, num in enumerate(line.strip()):
            heightmap[i + 1j * j] = int(num)


def neighbors(point):
    return [point - 1, point + 1, point - 1j, point + 1j]


def basin_size(point):
    if heightmap[point] == 9:
        return 0

    visited.add(point)

    size = 1
    for nbr in neighbors(point):
        if heightmap[point] < heightmap[nbr] and nbr not in visited:
            size += basin_size(nbr)

    return size


sum_ = 0
basins, visited = [], set()
for point in list(heightmap.keys()):
    if all(heightmap[point] < heightmap[nbr] for nbr in neighbors(point)):
        sum_ += heightmap[point] + 1
        basins.append(basin_size(point))

print(f"Day 9 part 1: {sum_}")

basins.sort()
largest = basins[-1] * basins[-2] * basins[-3]
print(f"Day 9 part 2: {largest}")
