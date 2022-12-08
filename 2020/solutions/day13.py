with open('../inputs/13.txt') as f:
    earliest = int(f.readline())
    buses = [0 if num == 'x' else int(num) for num in f.readline().split(',')]

minutes, bus = min((-earliest % b, b) for b in buses if b != 0)
print(f'Day 13 part 1: {bus*minutes}')

t, step = 1, 1
for i, b in enumerate(buses):
    if b != 0:
        while (t+i) % b != 0:
            t += step
        step *= b
print(f'Day 13 part 2: {t}')
