import heapq


def valid_moves(node, positions):
    amphipod, pos, floor = node
    occupied = {(i, j): a for a, i, j in positions}
    moves = []

    if any((pos, f) in occupied for f in range(0, floor)):
        return moves

    room = goal[amphipod]
    if pos == room:
        if all(
            occupied.setdefault((pos, f), None) == amphipod
            for f in range(floor + 1, floor_end)
        ):
            return moves

    cost = costs[amphipod]
    for start, end, step in [(pos - 1, hallway_start, -1), (pos + 1, hallway_end, 1)]:
        energy = cost * (floor + 1)
        for i in range(start, end, step):
            energy += cost

            if i == room:
                for f in range(floor_end - 1, -1, -1):
                    if (room, f) not in occupied:
                        moves.append([energy + cost * (f + 1), (amphipod, room, f)])
                        break
                    if occupied.setdefault((room, f), amphipod) != amphipod:
                        break

            if (i, -1) in occupied:
                break

            if floor != -1 and i not in rooms:
                moves.append([energy, (amphipod, i, -1)])

    return moves


def dijkstra(start_positions, end_positions):
    to_visit = [(0, start_positions)]
    energies = {frozenset(start_positions): 0}
    while to_visit:
        total_en, node = heapq.heappop(to_visit)

        if node == end_positions:
            return total_en

        for a in node:
            node_ = {p for p in node if p != a}
            for new_en, new_a in valid_moves(a, node_):
                en = new_en + total_en
                new_node = node_.union({new_a})
                f_new_node = frozenset(new_node)
                if f_new_node not in energies or en < energies[f_new_node]:
                    energies[f_new_node] = en
                    heapq.heappush(to_visit, (en, new_node))


hallway_start, hallway_end = -1, 11
rooms = [2, 4, 6, 8]
goal = {"A": 2, "B": 4, "C": 6, "D": 8}
costs = {"A": 1, "B": 10, "C": 100, "D": 1000}

with open("../inputs/23.txt") as f:
    lines = f.readlines()[2:4]
    positions = set(p for j in range(2) for p in zip(lines[j][3:10:2], rooms, [j] * 4))

floor_end = 2
end_positions = {(a, i, j) for a, i in goal.items() for j in range(floor_end)}
print(f"Day 23 part 1: {dijkstra(positions, end_positions)}")

extra_positions = {
    ("D", 2, 1), ("C", 4, 1), ("B", 6, 1), ("A", 8, 1),
    ("D", 2, 2), ("B", 4, 2), ("A", 6, 2), ("C", 8, 2),
}
positions = {p if p[2] == 0 else (p[0], p[1], 3) for p in positions}
positions = positions.union(extra_positions)

floor_end = 4
end_positions = {(a, i, j) for a, i in goal.items() for j in range(floor_end)}
print(f"Day 23 part 2: {dijkstra(positions, end_positions)}")
