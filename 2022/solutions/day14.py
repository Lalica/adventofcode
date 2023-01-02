def fall(cave, start):
    flooding = False
    while not flooding:
        sand = start

        falling = True
        while falling:
            for to_go in [sand + 1j, sand - 1 + 1j, sand + 1 + 1j]:
                if to_go not in cave:
                    flooding = True
                    falling = False
                    break
                elif cave[to_go] == ".":
                    sand = to_go
                    break
            else:
                if cave[sand] != ".":
                    flooding = True
                else:
                    cave[sand] = "o"
                falling = False


def mark_empty_spaces(cave, ceiling, with_floor=False):
    cave = cave.copy()

    min_x = int(min(pos.real for pos in cave) - 1)
    max_x = int(max(pos.real for pos in cave) + 1)
    min_y = int(ceiling)
    max_y = int(max(pos.imag for pos in cave) + 1)

    if with_floor:
        min_x -= 150
        max_x += 150
        j = max_y + 1
        for i in range(min_x, max_x + 1):
            cave[i + j*1j] = "#"
    
    for j in range(min_y, max_y + 1):
        for i in range(min_x, max_x + 1):
            if i + j*1j not in cave:
                cave[i + j*1j] = "."

    return cave


with open("../inputs/14.txt") as f:
    cave = dict()
    start = 500 + 0j
    for line in f.read().splitlines():
        dots = [tuple(map(int, dot.split(","))) for dot in line.split(" -> ")]

        for i in range(len(dots) - 1):
            x1, y1 = dots[i]
            x2, y2 = dots[i + 1]

            if x1 == x2:
                for j in range(min(y1, y2), max(y1, y2) + 1):
                    cave[x1 + j*1j] = "#"
            else:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    cave[i + y1*1j] = "#"

small_cave = mark_empty_spaces(cave, start.imag)
fall(small_cave, start)
part1 = sum(c == "o" for c in small_cave.values())
print(f'Day 14 part 1: {part1}')

big_cave = mark_empty_spaces(cave, start.imag, with_floor=True)
fall(big_cave, start)
part2 = sum(c == "o" for c in big_cave.values())
print(f'Day 14 part 2: {part2}')
