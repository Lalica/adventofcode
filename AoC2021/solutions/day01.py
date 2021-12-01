with open("../inputs/01.txt") as f:
    depth = list(map(int, f))
    n = len(depth)

part1 = sum(depth[i] > depth[i-1] for i in range(1, n))
print(f'Day 1 part 1: {part1}')

part2 = sum(sum(depth[i-3:i]) > sum(depth[i-4:i-1]) for i in range(4, n+1))
print(f'Day 1 part 2: {part2}')
