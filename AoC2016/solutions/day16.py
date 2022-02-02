def checksum(initial, disk_length):
    disk = initial.copy()
    while len(disk) < disk_length:
        disk += ["0"] + ["0" if i == "1" else "1" for i in reversed(disk)]

    disk = list(map(int, disk[:disk_length]))

    while len(disk) % 2 == 0:
        d1 = disk[: disk_length: 2]
        d2 = disk[1: disk_length: 2]
        disk = [not (b1 ^ b2) for b1, b2 in zip(d1, d2)]

    return "".join(map(lambda x: str(int(x)), disk))


with open("../inputs/16.txt") as f:
    initial = list(f.read().strip())

print(f"Day 16 part 1: {checksum(initial, 272)}")
print(f"Day 16 part 2: {checksum(initial, 35651584)}")
