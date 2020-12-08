with open('../inputs/08.txt') as f:
    instructions = [line.strip().split(' ') for line in f]

change_i = -1
while True:
    i, acc = 0, 0
    visited = {len(instructions)}
    while i not in visited:
        code, num = instructions[i]
        num = int(num)

        visited.add(i)

        if code == 'nop':
            i += 1
        if code == 'acc':
            acc += num
            i += 1
        if code == 'jmp':
            i += num
    if i == len(instructions):
        print(f'Day 8 part 2: {acc}')
        break

    if change_i == -1:
        print(f'Day 8 part 1: {acc}')
    else:
        instructions[change_i][0] = 'jmp' if instructions[change_i][0] == 'nop' else 'nop'
    change_i += 1

    while instructions[change_i][0] == 'acc':
        change_i += 1
    instructions[change_i][0] = 'jmp' if instructions[change_i][0] == 'nop' else 'nop'
