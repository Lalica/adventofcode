with open("../inputs/08.txt") as f:
    instructions = f.read().strip().split("\n")

n, m = 6, 50
screen = set()
for instruction in instructions:
    instruction = instruction.split()

    if instruction[0] == "rect":
        x, y = map(int, instruction[1].split("x"))
        for j in range(y):
            for i in range(x):
                screen.add((i, j))

    elif instruction[0] == "rotate":
        is_row = instruction[1] == "row"
        k = int(instruction[2].split("=")[1])
        offset = int(instruction[4])

        new_screen = set()
        for i, j in screen:
            if is_row and j == k:
                i = (i + offset) % m
            elif not is_row and i == k:
                j = (j + offset) % n
            new_screen.add((i, j))

        screen = new_screen

print(f"Day 8 part 1: {len(screen)}")

print("Day 8 part 2:")
for j in range(n):
    line = "".join("#" if (i, j) in screen else " " for i in range(m))
    print(line)
