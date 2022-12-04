from computer import opcode


def run(data, noun, verb):
    data[1] = noun
    data[2] = verb
    return opcode(data)


with open('../inputs/02.txt') as f:
    data = list(map(int, f.read().strip().split(',')))

part1 = run(data[:], 12, 2)
print(f'Day 2 part 1: {part1}')

output = 19690720
part2 = next(noun * 100 + verb
        for noun in range(100)
        for verb in range(100)
        if run(data[:], noun, verb) == output) 
print(f'Day 2 part 2: {part2}')
