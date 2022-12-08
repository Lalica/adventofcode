from collections import defaultdict


def recurse(node, path, twice=False):
    if node == "end":
        return 1

    paths = 0
    for nbr in graph[node]:
        visited_small = nbr.islower() and nbr in path
        if not visited_small or (not twice and nbr != "start"):
            paths += recurse(nbr, path + " " + nbr, twice or visited_small)

    return paths


graph = defaultdict(list)
with open("../inputs/12.txt") as f:
    for line in f:
        a, b = line.strip().split("-")
        graph[a].append(b)
        graph[b].append(a)

part1 = recurse("start", "start", True)
print(f"Day 12 part 1: {part1}")

part2 = recurse("start", "start")
print(f"Day 12 part 2: {part2}")
