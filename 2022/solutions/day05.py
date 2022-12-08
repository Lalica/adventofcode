import re


with open("../inputs/05.txt") as f:
    containers, moves = f.read().split('\n\n')

    cols = list(''.join(col) for col in zip(*containers.splitlines()))
    containers = [list(cols[i].strip()[:-1])[::-1] for i in range(1, len(cols), 4)]
    containers2 = [col[:] for col in containers]

for move in moves.splitlines():
    num, i, j = map(int, re.findall(r'\d+', move))

    containers[j - 1] += containers[i - 1][-num:][::-1]
    del containers[i - 1][-num:]

    containers2[j - 1] += containers2[i - 1][-num:]
    del containers2[i - 1][-num:]

part1 = ''.join(container[-1] for container in containers)
print(f'Day 5 part 1: {part1}')

part2 = ''.join(container[-1] for container in containers2)
print(f'Day 5 part 2: {part2}')
