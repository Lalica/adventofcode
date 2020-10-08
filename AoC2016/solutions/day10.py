from collections import namedtuple

Item = namedtuple("Item", ["name", "is_gen"])

with open("../inputs/10.txt") as f:
    data = f.read().strip().splitlines()

    floors = []
    for line in data:
        floor = []
        for word in line.split(" a "):
            if "generator" in word:
                floor.append(Item(word.split()[-2], True))
            elif "microchip" in word:
                floor.append(Item(word.split()[-2].split("-")[0], False))
        floors.append(floor)

print(floors)

