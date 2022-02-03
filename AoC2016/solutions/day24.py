from heapq import heappush, heappop


def get_neighbours(node):
    x, y = node
    nbrs = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [(nbr, grid[nbr]) for nbr in nbrs if grid[nbr] != "#"]


grid, keys = {}, {}
with open("../inputs/24.txt") as f:
    for j, line in enumerate(f):
        for i, c in enumerate(line.strip()):
            grid[i, j] = c
            if c not in "#.":
                keys[c] = (i, j)

part1 = None
part2 = None
to_visit = []
heappush(to_visit, (0, len(keys) - 1, keys["0"], frozenset("0")))
seen = {(keys["0"], frozenset("0")): 0}
while to_visit:
    dist, keys_left, node, keys_picked = heappop(to_visit)
    if keys_left == 0:
        if part1 is None:
            part1 = dist

        if node == keys["0"]:
            part2 = dist
            break

    for nbr, key in get_neighbours(node):
        found_key = key in keys and key not in keys_picked
        kp = keys_picked | ({key} if found_key else set())
        kl = keys_left - 1 if found_key else keys_left

        if (nbr, kp) not in seen or seen[(nbr, kp)] > dist + 1:
            heappush(to_visit, (dist + 1, kl, nbr, kp))
            seen[(nbr, kp)] = dist + 1

print(f"Day 24 part 1: {part1}")
print(f"Day 24 part 2: {part2}")
