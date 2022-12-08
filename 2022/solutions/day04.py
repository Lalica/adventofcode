import re


with open("../inputs/04.txt") as f:
    pairs = [list(map(int, re.split(",|-", line))) for line in f]

part1 = sum((a >= x and b <= y) or (x >= a and y <= b) for a, b, x, y in pairs)
print(f'Day 4 part 1: {part1}')

part2 = len(pairs) - sum(b < x or y < a for a, b, x, y in pairs)
print(f'Day 4 part 2: {part2}')
