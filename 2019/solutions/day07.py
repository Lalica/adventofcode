from computer import read_file, opcode
from itertools import permutations


with open('../inputs/07.txt') as f:
# with open('tmp.txt') as f:
    data = read_file(f)


signals = []
for phase_settings in permutations(range(5)):
    output_list = [0]
    for i in range(5):
        input_iter = iter([phase_settings[i], output_list[0]])
        output_list = []
        opcode(data[:], input_iter, output_list)

    signals.append(output_list[0])
    
part1 = max(signals)
print(f'Day 7 part 1: {part1}')

signals = []
for phase_settings in permutations(range(5, 10)):
    output_list = [0]
    amplifiers = [data[:] for _ in range(5)]
    for i in range(5):
        input_iter = iter([phase_settings[i], output_list[0]])
        output_list = []
        amplifiers[i] = opcode(amplifiers[i], input_iter, output_list)

    run = True
    while(run):
        for i in range(5):
            input_iter = iter(output_list)
            output_list = []
            amplifiers[i] = opcode(amplifiers[i], input_iter, output_list)
            if isinstance(amplifiers[i], int):
                run = False
                signals.append(output_list)

part2 = max(signals)
print(f'Day 7 part 2: {part2}')
