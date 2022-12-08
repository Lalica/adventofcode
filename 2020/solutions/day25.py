with open('../inputs/25.txt') as f:
    card_pc, door_pc = map(int, f)

subject_num = 7
mod = 20201227
loop_size = -1

found = -1
while found != card_pc and found != door_pc:
    loop_size += 1
    found = pow(subject_num, loop_size, mod)

pc = card_pc if found == door_pc else door_pc
print(f'Day 25 part 1: {pow(pc, loop_size, mod)}')
