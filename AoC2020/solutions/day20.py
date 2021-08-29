from collections import defaultdict
from math import sqrt


def rotate(tile):
    n = len(tile)
    new_tile = [["." for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_tile[j][n - i - 1] = tile[i][j]

    return ["".join(t) for t in new_tile]


def flip(tile):
    return [t[::-1] for t in tile]


def part_1(corners):
    mul = 1
    for c in corners:
        mul *= c
    print(f"Day 20 part 1: {mul}")


def solve(tiles, monster):
    neighbours = get_neighbours(tiles)
    m = 10 - 2

    n = int(sqrt(len(tiles)))
    grid = [["" for _ in range(n)] for _ in range(n * m)]

    corners = [n for n, t in neighbours.items() if len(t) == 2]
    part_1(corners)

    current = corners[0]
    current_t = place_first_corner(grid, current, neighbours, m)
    placed = [current]

    place(current, current_t, 0, 0, grid, tiles, neighbours, placed)

    grid = ["".join(g) for g in grid]
    part2(grid, monster)


def place_first_corner(grid, corner, neighbours, m):
    tile = tiles[corner]
    n1, n2 = tiles[neighbours[corner][0]], tiles[neighbours[corner][1]]
    pos1, _ = position_tile(tile, n1)
    pos2, _ = position_tile(tile, n2)

    good1, good2 = pos1 in [1, 2], pos2 in [1, 2]

    if not good1:
        if not good2:
            tile = rotate(tile)
            tile = rotate(tile)
        else:
            tile = rotate(tile)
            if pos1 == 3:
                tile = rotate(tile)
                tile = rotate(tile)
    else:
        if not good2:
            tile = rotate(tile)
            if pos2 == 3:
                tile = rotate(tile)
                tile = rotate(tile)

    for i in range(m):
        grid[i][0] = tile[i + 1][1:-1]
    return tile


def place(cname, ctile, x, y, grid, tiles, neighbours, placed):
    m = 10 - 2
    for neighbour in neighbours[cname]:
        if neighbour in placed:
            continue

        pos, tile = position_tile(ctile, tiles[neighbour])

        xn, yn = x, y
        if pos == 0:
            yn = y - m
        elif pos == 1:
            xn = x + 1
        elif pos == 2:
            yn = y + m
        elif pos == 3:
            xn = x - 1

        for i in range(m):
            grid[yn + i][xn] = tile[i + 1][1:-1]

        placed.append(neighbour)
        place(neighbour, tile, xn, yn, grid, tiles, neighbours, placed)


def get_neighbours(tiles):
    neighbours = defaultdict(list)

    for name in tiles:
        for name2 in tiles:
            if len(neighbours[name]) == 4:
                break
            if (len(neighbours[name2]) == 4 or name2 in neighbours[name]
                    or name == name2):
                continue

            if detect_match(name, name2, tiles):
                neighbours[name].append(name2)
                neighbours[name2].append(name)

    return neighbours


def detect_match(name, name2, tiles):
    tile, tile2 = tiles[name], tiles[name2]
    pos, _ = position_tile(tile, tile2)
    return pos != -1


def position_tile(tile, tile2):
    for _ in range(2):
        for _ in range(4):
            if tile[0] == tile2[-1]:
                return 0, tile2
            tile2 = rotate(tile2)

        side = "".join([t[-1] for t in tile])
        for _ in range(4):
            side2 = "".join([t[0] for t in tile2])
            if side == side2:
                return 1, tile2
            tile2 = rotate(tile2)

        for _ in range(4):
            if tile[-1] == tile2[0]:
                return 2, tile2
            tile2 = rotate(tile2)

        side = "".join([t[0] for t in tile])
        for _ in range(4):
            side2 = "".join([t[-1] for t in tile2])
            if side == side2:
                return 3, tile2
            tile2 = rotate(tile2)

        tile2 = flip(tile2)

    return -1, []


def find_monster(grid, monster):
    n = len(grid)

    for i in range(n - 3):
        for j in range(n - 19):
            monster_here = True

            for mi, mj in monster:
                if grid[i + mi][j + mj] != "#":
                    monster_here = False
                    break

            if monster_here:
                return True

    return False


def rough_waters(grid, monster):
    n = len(grid)
    grid = [[c for c in row] for row in grid]

    for i in range(n - 3):
        for j in range(n - 19):
            monster_here = True

            for mi, mj in monster:
                if grid[i + mi][j + mj] != "#":
                    monster_here = False
                    break

            if monster_here:
                for mi, mj in monster:
                    grid[i + mi][j + mj] = "O"

    return len([1 for row in grid for col in row if col == "#"])


def part2(grid, monster):
    for _ in range(2):
        for _ in range(4):
            if find_monster(grid, monster):
                cnt = rough_waters(grid, monster)
                print(f"Day 20 part 2: {cnt}")
                return
            grid = rotate(grid)
        grid = flip(grid)


with open("../inputs/20.txt") as f:
    data = f.read().split("\n\n")

tiles = {
    int(d.split("\n")[0].split(" ")[1][:-1]): d.strip().split("\n")[1:]
    for d in data
}
"""
                  #
#    ##    ##    ###
 #  #  #  #  #  #
"""
monster = [
    (1, 0),
    (2, 1),
    (2, 4),
    (1, 5),
    (1, 6),
    (2, 7),
    (2, 10),
    (1, 11),
    (1, 12),
    (2, 13),
    (2, 16),
    (1, 17),
    (0, 18),
    (1, 18),
    (1, 19),
]

solve(tiles, monster)
