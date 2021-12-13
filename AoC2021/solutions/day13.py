def fold(dots, axis, num):
    new_dots = set()
    for dot in dots:
        dot = {"x": dot[0], "y": dot[1]}

        if dot[axis] >= num:
            dot[axis] = 2 * num - dot[axis]

        new_dots.add((dot["x"], dot["y"]))

    return new_dots


with open("../inputs/13.txt") as f:
    dots, instructions = f.read().strip().split("\n\n")
    dots = {tuple(map(int, line.split(","))) for line in dots.split("\n")}

for i, instruction in enumerate(instructions.split("\n")):
    axis, num = instruction.split("=")

    dots = fold(dots, axis[-1], int(num))
    if i == 0:
        print(f"Day 12 part 1: {len(dots)}")

print("Day 12 part 2:")
X, Y = zip(*dots)
for y in range(max(Y) + 1):
    print("".join(" #"[(x, y) in dots] for x in range(max(X) + 1)))
