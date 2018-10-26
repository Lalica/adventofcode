with open("../inputs/01.txt") as f:
    input = f.read().strip()

print("Day 1 part 1: " + str(input.count("(") - input.count(")")))

floor = 0
for i in range(len(input)):
    if input[i] == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print("Day 1 part 2: " + str(i+1))
        break
