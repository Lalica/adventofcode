def move(arrow):
    if arrow == '^':
        return -10000
    elif arrow == 'v':
        return 10000
    elif arrow == '<':
        return -1
    elif arrow == '>':
        return 1


with open("../inputs/03.txt") as f:
    input = f.read().strip()

current, houses = 0, []
houses.append(current)

for i in range(len(input)):
    current += move(input[i])
    houses.append(current)
print("Day 3 part 1: " + str(len(set(houses))))

currentS, currentR, houses = 0, 0, []
houses.append(currentS)

for i in range(0, len(input), 2):
    currentS += move(input[i])
    houses.append(currentS)
    currentR += move(input[i+1])
    houses.append(currentR)
print("Day 3 part 2: " + str(len(set(houses))))
