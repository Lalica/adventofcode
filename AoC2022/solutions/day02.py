with open("../inputs/02.txt") as f:
    games = [(ord(line[0]) - ord('A') + 1, ord(line[2]) - ord('X') + 1) for line in f]

part1 = sum(y + ((y - x + 1) % 3) * 3 for x, y in games)
print(f'Day 2 part 1: {part1}')

part2 = sum((x + y) % 3 + 1 + (y - 1) * 3 for x, y in games)
print(f'Day 2 part 2: {part2}')
