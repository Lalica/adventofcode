from collections import defaultdict


with open('../inputs/10.txt') as f:
    adapters = [int(line) for line in f]
adapters.sort()

diff1, diff3 = 0, 1
prev = 0
for a in adapters:
    diff = a - prev
    if diff == 1:
        diff1 += 1
    elif diff == 3:
        diff3 += 1
    prev = a

ways = defaultdict(int)
ways[0] = 1
for a in adapters:
    ways[a] = ways[a-1] + ways[a-2] + ways[a-3]

print(f'Day 10 part 1: {diff3 * diff1}')
print(f'Day 10 part 2: {ways[adapters[-1]]}')
