import heapq


def is_open(pos):
    x, y = pos
    num = x * x + 3 * x + 2 * x * y + y + y * y
    num += fav_number
    return bin(num).count("1") % 2 == 0


def get_neighbours(pos):
    x, y = pos
    nbrs = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [nbr for nbr in nbrs if nbr[0] >= 0 and nbr[1] >= 0 and is_open(nbr)]


def dijkstra(start, end):
    seen = dict()
    seen[start] = 0
    to_visit = [(0, start)]

    part1 = None
    part2 = 0
    while to_visit:
        cost, node = heapq.heappop(to_visit)

        if node == end:
            part1 = cost

        if cost <= 50:
            part2 += 1
        elif part1:
            return part1, part2

        for nbr in get_neighbours(node):
            if nbr not in seen or seen[nbr] > cost + 1:
                seen[nbr] = cost + 1
                heapq.heappush(to_visit, (cost + 1, nbr))


with open("../inputs/13.txt") as f:
    fav_number = int(f.read())
start = (1, 1)
end = (31, 39)

part1, part2 = dijkstra(start, end)
print(f"Day 13 part 1: {part1}")
print(f"Day 13 part 2: {part2}")
