from itertools import count


def move(cucumbers, dir):
    moved = False
    new_cucumbers = set()
    for x, y in cucumbers:
        i, j = x, y
        if dir == ">":
            i = (x + 1) % m
        else:
            j = (y + 1) % n

        if (i, j) in east or (i, j) in south:
            new_cucumbers.add((x, y))
        else:
            moved = True
            new_cucumbers.add((i, j))

    return new_cucumbers, moved


with open("../inputs/25.txt") as f:
    map_ = [list(line.strip()) for line in f]
    n, m = len(map_), len(map_[0])

east = {(x, y) for y in range(n) for x in range(m) if map_[y][x] == ">"}
south = {(x, y) for y in range(n) for x in range(m) if map_[y][x] == "v"}

for step in count(1):
    east, moved_east = move(east, ">")
    south, moved_south = move(south, "v")

    if not moved_east and not moved_south:
        print(f"Day 25 part 1: {step}")
        break
