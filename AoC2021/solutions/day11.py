def flash(i, j):
    if (i, j) in flashed:
        return

    flashed.add((i, j))

    for nbr in neighbors(i, j):
        x, y = nbr
        octopuses[x][y] += 1
        if octopuses[x][y] > 9:
            flash(x, y)


def neighbors(i, j):
    nbrs = [
            (i-1, j-1), (i-1, j), (i-1, j+1),
            (i, j-1), (i, j+1),
            (i+1, j-1), (i+1, j), (i+1, j+1)
    ]
    return [(x, y) for x, y in nbrs if 0 <= x < 10 and 0 <= y < 10]


with open("../inputs/11.txt") as f:
    octopuses = [list(map(int, line.strip())) for line in f]

height, width = len(octopuses), len(octopuses[0])
sum_flashes = 0
step = 1
while True:
    flashed = set()

    for i in range(height):
        for j in range(width):
            octopuses[i][j] += 1
            if octopuses[i][j] > 9:
                flash(i, j)

    for i, j in flashed:
        octopuses[i][j] = 0

    sum_flashes += len(flashed)
    if step == 100:
        print(f"Day 11 part 1: {sum_flashes}")

    if len(flashed) == height * width:
        print(f"Day 11 part 2: {step}")
        break

    step += 1
