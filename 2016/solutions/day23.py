from math import factorial

with open("../inputs/23.txt") as fp:
    program = list(map(str.split, fp))

value1 = factorial(7) + int(program[19][1]) * int(program[20][1])
print(f"Day 23 part 1: {value1}")

value2 = factorial(12) + int(program[19][1]) * int(program[20][1])
print(f"Day 23 part 2: {value2}")
