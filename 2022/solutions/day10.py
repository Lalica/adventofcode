def inc_cycle(cycle, inc, signals, x, screen):
    for _ in range(inc):
        cycle += 1

        if cycle in [20, 60, 100, 140, 180, 220]:
            signals.append(cycle * x)

        if (cycle - 1) % 40 in [x -1, x, x + 1]:
            screen.append("#")
        else:
            screen.append(" ")

    return cycle


def computer(code, x=1):
    cycles = 0
    signals = []
    screen = []
    for line in code:
        if line == "noop":
            cycles = inc_cycle(cycles, 1, signals, x, screen)
        else:
            cycles = inc_cycle(cycles, 2, signals, x, screen)
            val = int(line.split()[1])
            x += val

    return signals, screen


with open("../inputs/10.txt") as f:
    program = f.read().splitlines()

signals, screen = computer(program)

part1 = sum(signals)
print(f'Day 10 part 1: {part1}')

for i in range(6):
    print("".join(screen[i * 40:i * 40 + 40]))
print(f'Day 10 part 2: READ LETTERS ABOVE')
