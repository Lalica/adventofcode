import re
from heapq import heappop, heappush


def get_neighbours(node, nodes):
    x, y = node
    nbrs = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [nbr for nbr in nbrs if nbr in nodes and nodes[nbr]]


def dijkstra(start, end, nodes):
    to_visit = [(0, start)]
    seen = {start: 0}
    while to_visit:
        dist, node = heappop(to_visit)
        if node == end:
            return dist

        for nbr in get_neighbours(node, nodes):
            if nbr not in seen or seen[nbr] > dist + 1:
                heappush(to_visit, (dist + 1, nbr))
                seen[nbr] = dist + 1


with open("../inputs/22.txt") as f:
    data = [list(map(int, re.findall(r"[0-9]+", line))) for line in f][2:]

cnt = 0
for x1, y1, _, used, _, _ in data:
    for x2, y2, _, _, avail, _ in data:
        if (x1 != x2 or y1 != y2) and used != 0 and used <= avail:
            cnt += 1
print(f"Day 22 part 1: {cnt}")

start, total = next(((x, y), total) for x, y, total, _, _, use in data if use == 0)
nodes = {(x, y): used <= total for x, y, _, used, _, _ in data}

max_x = max(x for x, *_ in data)
end = (max_x, 0)

dist = dijkstra(start, end, nodes)
steps = dist + 5 * (max_x - 1)
print(f"Day 22 part 2: {steps}")
