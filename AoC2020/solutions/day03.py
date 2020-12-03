with open('../inputs/03.txt') as f:
    forest = [line.strip() for line in f]

m, n = len(forest), len(forest[0])
part1, part2 = 0, 1
steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for step_x, step_y in steps:
    x, y = step_x, step_y
    trees = 0
    while y < m:
        if forest[y][x % n] == '#':
            trees += 1
        x, y = x + step_x, y + step_y

    if step_x == 3:
        part1 = trees
    part2 *= trees

print(f'Day 3 part 1: {part1}')
print(f'Day 3 part 2: {part2}')
