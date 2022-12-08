with open('../inputs/15.txt') as f:
    starting = list(map(int, f.readline().split(',')))

seen = dict((s, i+1) for i, s in enumerate(starting[:-1]))

current = starting[-1]
for i in range(len(starting), 30000000):
    previous = current
    current = (i - seen[current]) if previous in seen else 0
    seen[previous] = i

    if i == 2020:
        print(f'Day 15 part 1: {previous}')

print(f'Day 15 part 2: {current}')
