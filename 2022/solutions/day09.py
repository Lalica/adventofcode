def next_pos(pos, direction):
    step = {'R': 1, 'L': -1, 'U': 1j, 'D': -1j}
    return pos + step[direction]


def move_closer(pos1, pos2):
    real = pos2.real - pos1.real
    imag = pos2.imag - pos1.imag

    # touching
    if (abs(real) < 2 and abs(imag) < 2):
        return pos1

    if real != 0:
        pos1 += [-1, 1][real > 0]
    if imag != 0:
        pos1 += [-1j, 1j][imag > 0]
    return pos1


with open("../inputs/09.txt") as f:
    moves = f.read().splitlines()

head, tails = 0j, [0j] * 9
seen1 = {tails[0]}
seen2 = {tails[-1]}
for move in moves:
    direction, steps = move[0], int(move[1:])
    for step in range(steps):
        head = next_pos(head, direction)

        prev = head
        for i in range(len(tails)):
            tails[i] = move_closer(tails[i], prev)
            prev = tails[i]

        seen1.add(tails[0])
        seen2.add(tails[-1])

part1 = len(seen1)
print(f'Day 9 part 1: {part1}')

part2 = len(seen2)
print(f'Day 9 part 2: {part2}')
