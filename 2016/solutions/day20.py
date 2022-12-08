with open("../inputs/20.txt") as f:
    intervals = sorted(tuple(map(int, line.split("-"))) for line in f)

final = []
current = intervals[0]
for i in range(1, len(intervals)):
    next_ = intervals[i]
    if current[1] + 1 < next_[0]:
        final.append(current)
        current = next_
    else:
        current = (current[0], max(current[1], next_[1]))
final.append(current)

first = None
allowed = 0
start = 0
for current in final:
    if first is None and current[0] > start:
        first = start
    allowed += current[0] - start
    start = current[1] + 1
allowed += max(4294967296 - start, 0)

print(f"Day 20 part 1: {first}")
print(f"Day 20 part 2: {allowed}")
