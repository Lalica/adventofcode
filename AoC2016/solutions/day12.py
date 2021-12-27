def fibonacci(n):
    sqrt_5 = pow(5, 0.5)
    Phi = (1 + sqrt_5) / 2
    phi = (1 - sqrt_5) / 2
    return int((pow(Phi, n) - pow(phi, n)) / sqrt_5)


with open('../inputs/12.txt') as f:
    instructions = f.read().splitlines()
    n1 = int(instructions[2].split()[1])
    c = int(instructions[16].split()[1])
    d = int(instructions[17].split()[1])
    n2 = int(instructions[5].split()[1])

part1 = fibonacci(n1 + 2) + c * d
print(f"Day 12 part 1 : {part1}")

part2 = fibonacci(n1 + 2 + n2) + c * d
print(f"Day 12 part 2 : {part2}")
