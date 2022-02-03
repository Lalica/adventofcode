from collections import defaultdict
from itertools import count


def to_int(x, registers):
    return int(x) if x[-1].isdigit() else registers[x]


def solve(init_program):
    for i in count(1):
        program = init_program.copy()
        registers = defaultdict(int)
        registers["a"] = i
        output = 0

        ip = 0
        while ip < len(program):
            code, *args = program[ip]
            x = args[0]
            if len(args) > 1:
                y = args[1]

            if code == "inc":
                registers[x] += 1
            elif code == "dec":
                registers[x] -= 1
            elif code == "cpy":
                registers[y] = to_int(x, registers)
            elif code == "jnz":
                if to_int(x, registers) != 0:
                    ip += to_int(y, registers)
                    continue
            elif code == "tgl":
                x = to_int(x, registers) + ip
                if x >= len(program):
                    continue
                elif program[x][0] == "inc":
                    program[x][0] = "dec"
                elif len(program[x][1]) == 1:
                    program[x][0] = "inc"
                elif program[x][0] == "jnz":
                    program[x][0] = "cpy"
                elif len(program[x][1]) == 2:
                    program[x][0] = "jnz"
            elif code == "out":
                if to_int(x, registers) != output % 2:
                    break

                output += 1
                if output >= 50:
                    return i

            ip += 1


with open("../inputs/25.txt") as f:
    init_program = [line.split() for line in f]

print(f"Day 25 part 1: {solve(init_program)}")
