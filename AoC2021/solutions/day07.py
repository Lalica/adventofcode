with open("../inputs/07.txt") as f:
    positions = [int(num) for num in f.read().split(",")]

positions.sort()
mod = positions[len(positions) // 2]
part1 = sum(abs(num - mod) for num in positions)

mean = sum(positions) // len(positions)
part2 = sum(abs(num - mean) * (abs(num - mean) + 1) / 2 for num in positions)

print(f"Day 7 part 1: {part1}")
print(f"Day 7 part 2: {part2}")
