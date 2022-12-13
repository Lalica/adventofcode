from functools import cmp_to_key


def compare(packet1, packet2):
    for val1, val2 in zip(packet1, packet2):
        if isinstance(val1, int) and isinstance(val2, int):
            res = val1 - val2
        else:
            if isinstance(val1, int):
                val1 = [val1]
            if isinstance(val2, int):
                val2 = [val2]
            res = compare(val1, val2)

        if res != 0:
            return res

    return len(packet1) - len(packet2)


with open("../inputs/13.txt") as f:
    packets = [eval(line) for line in f if line.strip()]

in_order = 0
for i in range(0, len(packets), 2):
    if compare(packets[i], packets[i + 1]) < 0:
        in_order += i // 2 + 1

part1 = in_order
print(f'Day 13 part 1: {part1}')

packets += [[2], [6]]
packets.sort(key=cmp_to_key(compare))
i = packets.index([2]) + 1
j = packets.index([6]) + 1

part2 = i * j
print(f'Day 13 part 2: {part2}')
