from hashlib import md5
from heapq import heappush, heappop


def get_neighbours(pos, path):
    x, y = pos
    next_pos = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

    nbrs = []
    for i, c in enumerate(md5((passcode + path).encode()).hexdigest()[:4]):
        if c in "cbdef":
            x, y = next_pos[i]
            if 0 <= x <= end[0] and 0 <= y <= end[1]:
                nbrs.append([(x, y), "UDLR"[i]])

    return nbrs


with open("../inputs/17.txt") as f:
    passcode = f.read().strip()

end = (3, 3)
to_visit = [(0, (0, 0), "")]
first = last = None

while to_visit:
    dist, node, path = heappop(to_visit)

    if node == end:
        if first is None:
            first = path
        last = len(path)
        continue

    for nbr, direction in get_neighbours(node, path):
        heappush(to_visit, (dist + 1, nbr, path + direction))

print(f"Day 17 part 1: {first}")
print(f"Day 17 part 1: {last}")
