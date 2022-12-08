with open('../inputs/01.txt') as f:
    masses = list(map(int, f))

part1 = sum(mass // 3 - 2 for mass in masses)
print(f'Day 1 part 1: {part1}')

total_fuel = lambda x: x + total_fuel(x // 3 - 2) if x > 0 else 0
part2 = sum(total_fuel(mass // 3 - 2) for mass in masses)
print(f'Day 1 part 2: {part2}')
