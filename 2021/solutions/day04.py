boards = []
with open("../inputs/04.txt") as f:
    numbers = list(map(int, next(f).split(",")))
    next(f)

    board = []
    for line in f:
        if line[:-1]:
            board.append([[int(num), False] for num in line.split()])
        else:
            boards.append(board)
            board = []

n = len(boards[0])
m = len(boards[0][0])
won = [False] * len(boards)
for num in numbers:
    for i in range(len(boards)):
        row_i, col_i = next(
            ([r, c] for r in range(n) for c in range(m) if num == boards[i][r][c][0]),
            [-1, -1],
        )

        if won[i] or row_i == -1:
            continue

        boards[i][row_i][col_i][1] = True

        row_marks = [col[1] for col in boards[i][row_i]]
        col_marks = [row[col_i][1] for row in boards[i]]
        if all(row_marks) or all(col_marks):
            won[i] = True

            part2 = sum(num for row in boards[i] for num, mark in row if not mark) * num
            if sum(won) == 1:
                part1 = part2

print(f"Day 4 part 1: {part1}")
print(f"Day 4 part 2: {part2}")
