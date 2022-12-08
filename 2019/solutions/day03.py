def find_dots(moves):
    dots = list()
    pos = 0j
    direction = {'L': 1, 'R': -1, 'U': 1j, 'D': -1j}
    for move, num in moves:
        dots += [pos + i * direction[move] for i in range(1, num + 1)]
        pos += num * direction[move]

    return dots


with open('../inputs/03.txt') as f:
    lines = [[(move[0], int(move[1:])) for move in line.split(',')] for line in f]

line1 = find_dots(lines[0])
line2 = find_dots(lines[1])
intersections = set(line1) & set(line2)

part1 = int(min(abs(num.real) + abs(num.imag) for num in intersections))
print(f'Day 2 part 1: {part1}')

part2 = min(line1.index(dot) + line2.index(dot) + 2 for dot in intersections)
print(f'Day 2 part 2: {part2}')
