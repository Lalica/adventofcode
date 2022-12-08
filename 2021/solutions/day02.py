horizontal, depth1, depth2, aim = 0, 0, 0, 0

with open("../inputs/02.txt") as f:
    for line in f:
        instruction, value = line.split()
        value = int(value)

        if instruction == "forward":
            horizontal += value
            depth2 += (value * aim)
        elif instruction == "down":
            depth1 += value
            aim += value
        else:  # instruction == "up"
            depth1 -= value
            aim -= value

print(f'Day 2 part 1: {horizontal * depth1}')
print(f'Day 2 part 2: {horizontal * depth2}')
