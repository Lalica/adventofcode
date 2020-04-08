import heapq
items = {0: [1, 2], 1: [0, 2], 2: [0, 1]}


def transitions(x, y, item):
    neighbours = [(i, j) for i, j in [(x, y-1), (x-1, y), (x, y+1), (x+1, y)] if i >= 0 and j >= 0]
    return [(x, y, it, 7) for it in items[cave[y][x]]] +\
           [(i, j, item, 1) for i, j in neighbours if item != cave[j][i]]


with open('../inputs/22.txt') as f:
    depth = int(next(f).split(' ')[1])
    tx, ty = list(map(int, next(f).split(' ')[1].split(',')))
max_xy = ty * 2
cave = [x[:] for x in [[0] * max_xy] * max_xy]

for y in range(max_xy):
    for x in range(max_xy):
        if x == tx and y == ty:
            cave[y][x] = (0 + depth) % 20183
        elif y == 0:
            cave[y][x] = (x * 16807 + depth) % 20183
        elif x == 0:
            cave[y][x] = (y * 48271 + depth) % 20183
        else:
            cave[y][x] = (cave[y-1][x] * cave[y][x-1] + depth) % 20183
for y in range(max_xy):
    for x in range(max_xy):
        cave[y][x] = cave[y][x] % 3

print('Day 22 part 1: ' + str(sum(cave[y][x] for y in range(ty+1) for x in range(tx+1))))

is_goal = lambda x, y, item: x == tx and y == ty and item == 1
herusistic = lambda x, y: abs(tx - x) + abs(ty - y)
front = [(0, 0, 1, 0, 0)]
seen = {(1, 0, 0): 0}

while front:
    _, g, item, x, y = heapq.heappop(front)
    if is_goal(x, y, item):
        print('Day 22 part 2: ' + str(g))
        break
    if seen[(item, x, y)] < g:
        continue
    for next_x, next_y, next_item, cost in transitions(x, y, item):
        if (next_item, next_x, next_y) not in seen or seen[(next_item, next_x, next_y)] > g+cost:
            seen[(next_item, next_x, next_y)] = g+cost
            heapq.heappush(front, (herusistic(next_x, next_y) + g + cost, g + cost, next_item, next_x, next_y))
