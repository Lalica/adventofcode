def run_program():
    while registers[ip] < len(instructions):
        op, a, b, c = instructions[registers[ip]].split()
        registers[int(c)] = operations[op](registers, int(a), int(b))
        registers[ip] += 1


operations = {"addr": lambda r, a, b: r[a] + r[b],
              "addi": lambda r, a, b: r[a] + b,
              "mulr": lambda r, a, b: r[a] * r[b],
              "muli": lambda r, a, b: r[a] * b,
              "banr": lambda r, a, b: r[a] & r[b],
              "bani": lambda r, a, b: r[a] & b,
              "borr": lambda r, a, b: r[a] | r[b],
              "bori": lambda r, a, b: r[a] | b,
              "setr": lambda r, a, b: r[a],
              "seti": lambda r, a, b: a,
              "gtir": lambda r, a, b: 1 if a > r[b] else 0,
              "gtri": lambda r, a, b: 1 if r[a] > b else 0,
              "gtrr": lambda r, a, b: 1 if r[a] > r[b] else 0,
              "eqir": lambda r, a, b: 1 if a == r[b] else 0,
              "eqri": lambda r, a, b: 1 if r[a] == b else 0,
              "eqrr": lambda r, a, b: 1 if r[a] == r[b] else 0}
instructions = open("../inputs/19.txt").read().strip().splitlines()
ip = int(instructions.pop(0)[4])
registers = [0] * 6
run_program()
print("Day 19 part 1: " + str(registers[0]))
print("Day 19 part 2: " + str(sum(i for i in range(1, 10551301) if 10551300 % i == 0)))

# registers = [0] * 6
# registers[1] = 10 551 300  # 2 * 2 * 19 * 11 + (2 * 22 + 20) + (27 * 28 + 29) * 30 * 14 * 32
# registers[5] = 1
# registers[4] = 1
# while True:
#     registers[2] = registers[5] * registers[4]
#     if registers[2] == registers[1]:
#         registers[0] += registers[5]
#     registers[4] += 1
#     if registers[4] > registers[1]:
#         registers[5] += 1
#         if registers[5] > registers[1]:
#             break
#         else:
#             registers[4] = 1
