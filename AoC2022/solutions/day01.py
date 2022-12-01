with open("../inputs/01.txt") as f:
    calories = [sum(map(int, elf.split())) for elf in f.read().split("\n\n")]

part1 = max(calories)
print(f'Day 1 part 1: {part1}')

part2 = sum(sorted(calories)[-3:])
print(f'Day 1 part 2: {part2}')
