import heapq


def is_safe(item, floor):
    unsafe_items = [i for i in floor if (i[0], not i[1]) not in floor]

    if item[0] in [i[0] for i in unsafe_items]:
        return True

    return all(i[1] == item[1] for i in unsafe_items)


def is_valid(items, floor):
    floor = [i for i in floor if i not in items]
    unsafe_items = [i for i in floor if (i[0], not i[1]) not in floor]

    return sum(i[1] for i in unsafe_items) == len(unsafe_items)


def valid_moves(floor, items):
    moves = []
    floors = [[], [], [], []]
    for i, (m, g) in enumerate(items):
        floors[m].append((i, True))
        floors[g].append((i, False))

    for next_floor in [floor - 1, floor + 1]:
        if next_floor < 0 or next_floor >= len(floors):
            continue

        for i, item in enumerate(floors[floor]):
            if is_safe(item, floors[next_floor]) and is_valid([item], floors[floor]):
                moves.append([next_floor, [item]])

            for j in range(i+1, len(floors[floor])):
                item2 = floors[floor][j]

                if item[0] == item2[0] and next_floor > floor:
                    moves.append([next_floor, [item, item2]])
                elif item[1] == item2[1] and is_safe(item2, floors[next_floor]) and is_valid([item], floors[floor]):
                    moves.append([next_floor, [item, item2]])

    return moves


def heuristic(items):
    return -sum(i[0] + i[1] for i in items)


def neighbours(state):
    elevator, items = state
    new_states = []
    for floor, moved_items in valid_moves(elevator, items):
        microchips = {i: f[0] for i, f in enumerate(items)}
        generators = {i: f[1] for i, f in enumerate(items)}
        for item in moved_items:
            if item[1]:
                microchips[item[0]] = floor
            else:
                generators[item[0]] = floor
        new_items = tuple((microchips[i], generators[i]) for i in range(n))

        new_states.append((floor, new_items))

    return new_states


def dijkstra(start, end):
    visit = [(0, 0, start)]
    seen = {start: 0}

    while len(visit):
        _, cost, node = heapq.heappop(visit)

        if node == end:
            return cost

        for nbr in neighbours(node):
            if nbr not in seen or seen[nbr] > cost + 1:
                seen[nbr] = cost + 1
                heapq.heappush(visit, (heuristic(nbr[1]), cost + 1, nbr))


microchips = dict()
generators = dict()
with open("../inputs/11.txt") as f:
    for floor, line in enumerate(f):
        for word in line.split(" a "):
            if "generator" in word:
                generators[word.split()[0]] = floor
            elif "microchip" in word:
                microchips[word.split()[0].split("-")[0]] = floor

n = len(microchips)

for part in range(1, 3):
    start_items = tuple((microchips[name], generators[name]) for name in microchips)
    start_state = (0, start_items)
    end_items = tuple((3, 3) for _ in range(n))
    end_state = (3, end_items)

    print(f"Day 11 part {part}: {dijkstra(start_state, end_state)}")

    microchips["elerium"] = 0
    microchips["dilithium"] = 0
    generators["elerium"] = 0
    generators["dilithium"] = 0
    n = len(microchips)
