from itertools import combinations
from functools import reduce
from operator import mul


with open("../inputs/24.txt") as f:
    packages = [int(num) for num in f]

target1, target2 = sum(packages) // 3, sum(packages) // 4
part1, part2 = 0, 0

for i in range(1, len(packages) + 1):
    groups = list(combinations(packages, i))

    group1 = [reduce(mul, group) for group in groups if sum(group) == target1]
    part1 = part1 if part1 else min(group1 or [0])

    group2 = [reduce(mul, group) for group in groups if sum(group) == target2]
    part2 = part2 if part2 else min(group2 or [0])

    if part1 and part2:
        break

print(f"Day 24 part 1: {part1}")
print(f"Day 24 part 2: {part2}")
