def move(neighbors, x, y, allies, enemies, cave_map):
    queue = []
    visited = {(x, y)}
    possible = {}
    for n in neighbors:
        if n in enemies:
            return x, y
        if n not in allies and cave_map[n[1]][n[0]] != '#':
            queue.append([n, n, 1])
            visited.add(n)
    while len(queue) > 0:
        n, d, m = queue.pop(0)
        for ax, ay in around(n[0], n[1]):
            if cave_map[ay][ax] == '#' or (ax, ay) in allies or (ax, ay) in visited:
                continue
            if (ax, ay) in enemies:
                if n not in possible or m < possible[n][1] or d[1] < possible[n][0][1] or (d[1] == possible[n][0][1] and d[0] < possible[n][0][0]):
                    possible[n] = [d, m]
            else:
                queue.append([(ax, ay), d, m+1])
            visited.add((ax, ay))
    return possible[sorted(possible.keys(), key=lambda tup: (tup[1], tup[0])).pop(0)][0] if len(possible) > 0 else (x, y)


def fight(xi, yi, allies, enemies, cave_map, c, hit):
    x, y = move(around(xi, yi), xi, yi, allies, enemies, cave_map)
    if (x, y) != (xi, yi):
        allies[(x, y)] = allies.pop((xi, yi))

        cave_map[yi] = cave_map[yi][:xi] + '.' + cave_map[yi][xi + 1:]
        cave_map[y] = cave_map[y][:x] + c + cave_map[y][x+1:]

    lowest = (x, y)
    for a in around(x, y):
        if a in enemies and (lowest not in enemies or enemies[a] < enemies[lowest]):
                lowest = a
    if lowest in enemies:
        enemies[lowest] -= hit
        if enemies[lowest] < 1:
            enemies.pop(lowest)
            
            cave_map[lowest[1]] = cave_map[lowest[1]][:lowest[0]] + '.' + cave_map[lowest[1]][lowest[0] + 1:]
    return x, y


def part1(elves, goblins, cave_map):
    counter = 0
    while len(elves) and len(goblins):
        # print(counter)
        # for b in range(len(cave_map)):
        #     print(cave_map[b])
        # sleep(0.5)
        moved = set()
        for j in range(len(cave_map)):
            for i in range(len(cave_map[0])):
                if len(elves) == 0 or len(goblins) == 0:
                    print(counter)
                    print(sum(elves.values() if len(elves) > 0 else goblins.values()))
                    return counter * sum(elves.values() if len(elves) > 0 else goblins.values())
                if (i, j) in goblins and (i, j) not in moved:
                    moved.add(fight(i, j, goblins, elves, cave_map, 'G', 3))
                elif (i, j) in elves and (i, j) not in moved:
                    moved.add(fight(i, j, elves, goblins, cave_map, 'E', 3))
        counter += 1
    return counter * sum(elves.values() if len(elves) > 0 else goblins.values())


def part2(elves, goblins, cave_map, elves_hit):
    counter, no_elves = 0, len(elves)
    while len(elves) and len(goblins):
        moved = set()
        # print(counter)
        # for b in range(len(cave_map)):
        #     print(cave_map[b])
        # sleep(0.5)
        for j in range(len(cave_map)):
            for i in range(len(cave_map[0])):
                if no_elves > len(elves):
                    return -1
                if len(goblins) == 0:
                    return counter * sum(elves.values())
                if (i, j) in goblins and (i, j) not in moved:
                    moved.add(fight(i, j, goblins, elves, cave_map, 'G', 3))
                elif (i, j) in elves and (i, j) not in moved:
                    moved.add(fight(i, j, elves, goblins, cave_map, 'E', elves_hit))
        counter += 1
    # print(counter)
    # for b in range(len(cave_map)):
    #     print(cave_map[b])
    return counter * sum(elves.values())


data = open("../inputs/15.txt").read().strip().splitlines()
around = lambda x, y: [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]

g, e = {}, {}
for j in range(len(data)):
    for i in range(len(data[0])):
        if data[j][i] == 'G':
            g[(i, j)] = 200
        elif data[j][i] == 'E':
            e[(i, j)] = 200

print("Day 15 part 1: " + str(part1(dict(e), dict(g), data[:])))

eh = 4
while part2(dict(e), dict(g), data[:], eh) == -1:
    eh += 1
print("Day 15 part 2: " + str(part2(dict(e), dict(g), data[:], eh)))
