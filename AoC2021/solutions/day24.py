with open("../inputs/24.txt") as f:
    instructions = f.read().split("inp w\n")[1:]

z = []
rules = []
for i, ins in enumerate(instructions):
    lines = ins.split("\n")
    push = int(lines[3].split()[-1]) == 1
    a = int(lines[4].split()[-1])
    b = int(lines[14].split()[-1])

    if push:
        z.append((i, b))
    else:
        j, b = z.pop()
        rules.append((j, b + a, i))

max_valid = [0] * 14
min_valid = [0] * 14
for i, x, j in rules:
    if x < 0:
        max_valid[i] = 9
        max_valid[j] = 9 + x

        min_valid[i] = 1 - x
        min_valid[j] = 1
    elif x > 0:
        max_valid[i] = 9 - x
        max_valid[j] = 9

        min_valid[i] = 1
        min_valid[j] = 1 + x
    else:
        max_valid[i] = 9
        max_valid[j] = 9

        min_valid[i] = 1
        min_valid[j] = 1

max_valid = int("".join(map(str, max_valid)))
min_valid = int("".join(map(str, min_valid)))
print(f"Day 24 part 1: {max_valid}")
print(f"Day 24 part 2: {min_valid}")
