def game(cups, current, iterations):
    for _ in range(iterations):
        first = cups[current]
        second = cups[first]
        third = cups[second]

        dest = (current - 1) % size
        while dest in (first, second, third):
            dest = (dest - 1) % size

        cups[current], cups[dest], cups[third] = cups[third], first, cups[dest]
        current = cups[current]

    return cups


with open('../inputs/23.txt') as f:
    initial = list(map(int, f.read().strip()))

size, iterations = len(initial), 100
cups = [0] * size
for i, num in enumerate(initial):
    cups[num - 1] = initial[(i + 1) % size] - 1

part1 = game(cups[:], initial[0] - 1, iterations)
after_one = [part1[0] + 1]
for _ in range(size - 2):
    after_one.append(part1[after_one[-1] - 1] + 1)
print('Day 23 part 1: ' + ''.join(map(str, after_one)))

cups[initial[-1] - 1] = size
size, iterations = 10**6, 10**7
cups = cups + list(range(len(cups) + 1, size)) + [initial[0] - 1]
part2 = game(cups, initial[0] - 1, iterations)
print(f'Day 23 part 2: {(part2[0] + 1) * (part2[part2[0]] + 1)}')
