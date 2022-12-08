from collections import defaultdict
from itertools import accumulate


with open("../inputs/07.txt") as f:
    terminal = f.read().splitlines()

dirs = defaultdict(int)
stack = []
for line in terminal:
    if line == "$ ls" or line.startswith("dir"):
        continue

    if line.startswith("$ cd"):
        path = line.split()[2]
        if path == "..":
            stack.pop()
        elif path == "/":
            stack = ["/"]
        else:
            stack.append(path)
    else:
        size = int(line.split()[0])
        for path in accumulate(stack, func=lambda a, b: a + "/" + b):
            dirs[path] += size

part1 = sum(size for size in dirs.values() if size <= 100000)
print(f'Day 7 part 1: {part1}')

space_required = dirs["/"] - 40000000
part2 = min(size for size in dirs.values() if size >= space_required)
print(f'Day 7 part 2: {part2}')
