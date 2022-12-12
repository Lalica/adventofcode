from heapq import heappop, heappush


def neighbours(pos):
    x, y = pos
    nbrs = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [n for n in nbrs if n in grid and ord(grid[n]) - ord(grid[pos]) < 2]


def walk(start, end):
    queue = [(0, start)]
    seen = set()
    while queue:
        steps, pos = heappop(queue)

        if pos == end:
            return steps

        if pos in seen:
            continue
        seen.add(pos)

        for neighbour in neighbours(pos):
            heappush(queue, (steps + 1, neighbour))

    return float("inf")


with open("../inputs/12.txt") as f:
    grid = {(x, y): c for y, line in enumerate(f) for x, c in enumerate(line.strip())}

    start_end = [0, 0]
    az = list("az")
    for key, value in grid.items():
        if value in "SE":
            start_end[value == "E"] = key
            grid[key] = az[value == "E"]

start, end = start_end
part1 = walk(start, end)
print(f'Day 12 part 1: {part1}')

steps = []
for start, value in grid.items():
    if value == "a":
        steps.append(walk(start, end))
part2 = min(steps)
print(f'Day 12 part 2: {part2}')
