with open('../inputs/12.txt') as f:
    data = [line.strip() for line in f]

ship1, ship2 = 0, 0
facing, waypoint = 1, 10 + 1j
directions = {'N': 1j, 'W': -1, 'S': -1j, 'E': 1}

for d in data:
    letter, value = d[0], int(d[1:])
    if letter == 'F':
        ship1 += facing*value
        ship2 += waypoint*value
    elif letter == 'R':
        facing /= 1j ** (value//90)
        waypoint /= 1j ** (value//90)
    elif letter == 'L':
        facing *= 1j ** (value//90)
        waypoint *= 1j ** (value//90)
    else:
        ship1 += directions[letter]*value
        waypoint += directions[letter]*value

print(f'Day 12 part 1: {int(abs(ship1.real) + abs(ship1.imag))}')
print(f'Day 12 part 2: {int(abs(ship2.real) + abs(ship2.imag))}')
