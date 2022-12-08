operations = {"AND": lambda x, y: x & y,
              "OR": lambda x, y: x | y,
              "RSHIFT": lambda x, y: x >> y,
              "LSHIFT": lambda x, y: x << y,
              "NOT": lambda x, y: ~y}


def find_value(i):
    if i.isdigit():
        return int(i)

    try:
        value = wires[i]
    except KeyError:
        return 0

    if value.isdigit():
        return int(value)

    if value.find(' ') == -1:
        return find_value(value)

    value = value.split()
    result = operations[value[-2]](find_value(value[0]), find_value(value[-1]))
    wires[i] = str(result)
    return result


with open("../inputs/07.txt") as f:
    input = {i.split("->")[-1].strip(): i.split("->")[0].strip() for i in f.read().strip().splitlines()}

wires = input.copy()
a = str(find_value("a"))
print("Day 7 part 1: " + a)

wires = input
wires["b"] = a
print("Day 7 part 2: " + str(find_value("a")))
