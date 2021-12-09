with open("../inputs/07.txt") as f:
    positions = [int(num) for num in f.read().split(",")]

positions.sort()
median = positions[len(positions) // 2]
medians = [median, median + 1]
part1 = [
        sum(abs(num - median) for num in positions)
        for median in medians
]

mean = sum(positions) // len(positions)
means = [mean, mean + 1]
part2 = [
        sum(abs(num - mean) * (abs(num - mean) + 1) // 2 for num in positions)
        for mean in means
]

print(f"Day 7 part 1: {min(part1)}")
print(f"Day 7 part 2: {min(part2)}")
