def recurse(containers, target, depth):
    if target == 0:
        combinations.append(depth)
        return

    if len(containers) == 0 or target < 0:
        return

    for i in range(len(containers)):
        recurse(containers[i + 1:], target - containers[i], depth + 1)


with open("../inputs/17.txt") as f:
    containers = list(map(int, f))
combinations = []

recurse(containers, 150, 1)
print(f"Day 17 part 1: {len(combinations)}")

min_num = min(combinations)
print(f"Day 17 part 2: {combinations.count(min_num)}")
