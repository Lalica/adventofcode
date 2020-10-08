from collections import defaultdict
import re

def rot(c, n):
    return chr((ord(c)-97+n)%26 + 97) if c != "-" else " "

with open("../inputs/04.txt") as f:
    data = f.read().strip().splitlines()

id_sum = 0
rooms = []
for line in data:
    groups = re.search(r"^(.*)-([0-9]+)\[(.*)\]$", line)
    name, s_id, checksum = groups.group(1), int(groups.group(2)), groups.group(3) 

    counter = defaultdict(int)
    for l in name:
        if l != "-":
            counter[l] += 1

    real_checksum = "".join([x[0] for x in \
            sorted(counter.items(), key=lambda x: (-x[1],x[0]))[:5]])

    if real_checksum == checksum:
        id_sum += s_id
        rooms.append((name, s_id))

print("Day 4 part 1: " + str(id_sum))

for room in rooms:
    decripted = "".join([rot(l, room[1]) for l in room[0]])
    if "north" in decripted:
        print("Day 4 part 2: " + str(room[1]))
        break

