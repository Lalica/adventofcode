from collections import defaultdict


def dfs(current, guests):
    if len(guests) == 0:
        return graph[frozenset([current, first])]

    max_sum = float("-inf")
    for guest in guests:
        happiness = graph[frozenset([guest, current])]
        max_sum = max(max_sum, happiness + dfs(guest, guests - {guest}))

    return max_sum


graph = defaultdict(int)
guests = set()
with open("../inputs/13.txt") as f:
    for name1, _, gain, value, *_, name2 in map(str.split, f):
        pair = frozenset([name1, name2[:-1]])
        happiness = int(value) * (-1)**(gain != "gain")

        graph[pair] += happiness
        guests.add(name1)

first = guests.pop()
part1 = dfs(first, guests)
print(f"Day 13 part 1: {part1}")

part2 = dfs(first, guests.union("me"))
print(f"Day 13 part 2: {part2}")
