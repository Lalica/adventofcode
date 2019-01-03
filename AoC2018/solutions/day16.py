from re import findall


operations = [lambda r, a, b: r[a] + r[b],
              lambda r, a, b: r[a] + b,
              lambda r, a, b: r[a] * r[b],
              lambda r, a, b: r[a] * b,
              lambda r, a, b: r[a] & r[b],
              lambda r, a, b: r[a] & b,
              lambda r, a, b: r[a] | r[b],
              lambda r, a, b: r[a] | b,
              lambda r, a, b: r[a],
              lambda r, a, b: a,
              lambda r, a, b: 1 if a > r[b] else 0,
              lambda r, a, b: 1 if r[a] > b else 0,
              lambda r, a, b: 1 if r[a] > r[b] else 0,
              lambda r, a, b: 1 if a == r[b] else 0,
              lambda r, a, b: 1 if r[a] == b else 0,
              lambda r, a, b: 1 if r[a] == r[b] else 0]

data = iter(open("../inputs/16.txt").read().strip().splitlines())
part1, done, numbers = 0, set(), {}
while True:
    before = map(int, findall("[0-9]+", next(data)))
    if len(before) == 0:
        next(data)
        break
    op, A, B, C = map(int, next(data).split())
    after = map(int, findall("[0-9]+", next(data)))
    next(data)
    possible = set(i for i, o in enumerate(operations) if o(before, A, B) == after[C])
    if len(possible) >= 3:
        part1 += 1
    possible = possible.difference(done)
    if not len(possible):
        continue
    if op not in numbers:
        numbers[op] = possible
    elif len(numbers[op]) != 1:
        numbers[op] = numbers[op].intersection(set(possible))
    if len(numbers[op]) == 1:
        num = numbers[op].pop()
        numbers[op] = [num]
        done.add(num)
        for k in numbers.keys():
            if k != op and num in numbers[k]:
                numbers[k].remove(num)

print("Day 16 part 1: " + str(part1))

registers = [0] * 4
for i in data:
    for o, A, B, C in [map(int, i.split())]:
        registers[C] = operations[numbers[o][0]](registers, A, B)
print("Day 16 part 2: " + str(registers[0]))
