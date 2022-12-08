def traverse(x_iter, y_iter, x_is_row, default_index, closest):
    for x in x_iter: 
        highest = -1
        last_seen = [default_index] * 10
        for y in y_iter:
            r, c = (x, y) if x_is_row else (y, x)
            tree = grid[r][c]

            visible[r][c] |= tree > highest
            highest = max(highest, tree)

            score[r][c] *= abs(y - closest(last_seen[tree:]))
            last_seen[tree] = y


with open("../inputs/08.txt") as f:
    grid = [list(map(int, line.strip())) for line in f]
    rows = len(grid)
    cols = len(grid[0])

visible = [[False] * cols for _ in range(rows)]
score = [[1] * cols for _ in range(rows)]

traverse(  # left
    x_iter=range(rows),
    y_iter=range(cols),
    x_is_row=True,
    default_index=0,
    closest=max
)
traverse(  # right
    x_iter=range(rows),
    y_iter=range(cols -1, -1, -1),
    x_is_row=True,
    default_index=cols - 1,
    closest=min
)
traverse(  # down
    x_iter=range(cols),
    y_iter=range(rows),
    x_is_row=False,
    default_index=0,
    closest=max
)
traverse(  # up
    x_iter=range(cols),
    y_iter=range(rows -1, -1, -1),
    x_is_row=False,
    default_index=rows - 1,
    closest=min
)

part1 = sum(map(sum, visible))
print(f'Day 8 part 1: {part1}')

part2 = max(map(max, score))
print(f'Day 8 part 2: {part2}')
