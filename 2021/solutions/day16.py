from functools import reduce
from operator import mul


def recurse(i, end, depth=-1):
    global version_sum
    literals = []

    if i == end or depth == 0 or len(packet) - i < 4:
        return i, literals

    version_sum += int(packet[i:i+3], 2)
    i += 3

    type_id = int(packet[i:i+3], 2)
    i += 3
    if type_id == 4:
        literal = ""

        last_packet = False
        while not last_packet:
            literal += packet[i+1:i+5]
            last_packet = packet[i] == "0"
            i += 5

        literals.append(int(literal, 2))
    else:
        if packet[i] == "0":
            length = int(packet[i+1:i+16], 2)
            i += 16
            i, op_literals = recurse(i, i + length, -1)
        else:
            num_subpackets = int(packet[i+1:i+12], 2)
            i += 12
            i, op_literals = recurse(i, end, num_subpackets)

        literals.append(operators[type_id](op_literals))

    i, new_literals = recurse(i, end, depth - 1)
    return i, literals + new_literals


with open("../inputs/16.txt") as f:
    packet = bin(int(f.read().strip(), 16))[2:]
    mod = len(packet) % 4
    if mod:
        packet = "0" * (4 - mod) + packet

operators = {
        0: lambda x: sum(x),
        1: lambda x: reduce(mul, x),
        2: lambda x: min(x),
        3: lambda x: max(x),
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1]),
}

version_sum = 0
_, value = recurse(0, len(packet))
print(f"Day 16 part 1: {version_sum}")
print(f"Day 16 part 2: {value[0]}")
