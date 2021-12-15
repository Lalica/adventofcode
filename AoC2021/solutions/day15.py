import heapq


def dijkstra(start, end):
    to_visit = [(0, start)]
    risks = {start: 0}

    while to_visit:
        total_risk, node = heapq.heappop(to_visit)

        if node == end:
            return total_risk

        for nbr in neighbors(*node):
            risk = get_risk(*nbr) + total_risk
            if nbr not in risks or risk < risks[nbr]:
                risks[nbr] = risk
                heapq.heappush(to_visit, (risk, nbr))


def neighbors(x, y):
    nbrs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [(i, j) for i, j in nbrs if 0 <= i < width and 0 <= j < height]


def get_risk(x, y):
    part_x, small_x, = divmod(x, small_width)
    part_y, small_y, = divmod(y, small_height)

    risk = graph[small_y][small_x] + part_x + part_y
    return risk - 9 if risk > 9 else risk


with open("../inputs/15.txt") as f:
    graph = [list(map(int, line.strip())) for line in f]
small_height, small_width = len(graph), len(graph[0])

height, width = small_height, small_width
part1 = dijkstra((0, 0), (width - 1, height - 1))
print(f"Day 15 part 1: {part1}")

height, width = small_height * 5, small_width * 5
part2 = dijkstra((0, 0), (width - 1, height - 1))
print(f"Day 15 part 2: {part2}")
