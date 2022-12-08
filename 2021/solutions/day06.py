with open("../inputs/06.txt") as f:
    fishes = list(map(int, next(f).split(",")))

cycle = [0] * 9
for fish in fishes:
    cycle[fish] += 1

for day in range(256):
    reached_end = cycle[0]
    for i in range(1, 9):
        cycle[i - 1] = cycle[i]
    cycle[8] = reached_end
    cycle[6] += reached_end
    if day == 79:
        print(f"Day 6 part 1: {sum(cycle)}")

print(f"Day 6 part 2: {sum(cycle)}")
