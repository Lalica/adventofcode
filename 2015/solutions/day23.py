def run():
    i = 0
    while i < len(instructions):
        instruction = instructions[i]

        if instruction[0] == "hlf":
            registers[instruction[1]] //= 2
            i += 1
        elif instruction[0] == "tpl":
            registers[instruction[1]] *= 3
            i += 1
        elif instruction[0] == "inc":
            registers[instruction[1]] += 1
            i += 1
        elif instruction[0] == "jmp":
            i += int(instruction[1])
        elif instruction[0] == "jie":
            if registers[instruction[1][:-1]] % 2 == 0:
                i += int(instruction[2])
            else:
                i += 1
        elif instruction[0] == "jio":
            if registers[instruction[1][:-1]] == 1:
                i += int(instruction[2])
            else:
                i += 1


with open("../inputs/23.txt") as f:
    instructions = [line.split() for line in f]

registers = {"a": 0, "b": 0, "c": 0}
run()
print(f"Day 23 part 1: {registers['b']}")

registers = {"a": 1, "b": 0, "c": 0}
run()
print(f"Day 23 part 1: {registers['b']}")
