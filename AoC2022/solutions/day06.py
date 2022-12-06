def first_n_distinct(data, n):
    for i in range(len(stream) - n):
        if len(set(stream[i:i + n])) == n:
            return i + n


with open("../inputs/06.txt") as f:
    stream = f.read().strip()

part1 = first_n_distinct(stream, 4)
print(f'Day 6 part 1: {part1}')

part2 = first_n_distinct(stream, 14)
print(f'Day 6 part 2: {part2}')
