with open("../inputs/01.txt") as f:
    data = f.read().strip().split(", ")

current = (0 + 0j)
current_dir = (0 + 1j)
directions = {
        ("R", 1j): (1 + 0j),
        ("R", 1): (0 - 1j),
        ("R", -1j): (-1 + 0j),
        ("R", -1): (0 + 1j),
        ("L", 1j): (-1 + 0j),
        ("L", -1): (0 - 1j),
        ("L", -1j): (1 + 0j),
        ("L", 1): (0 + 1j)} 

visited, done = set(), False
visited.add(0 + 0j)
for instruction in data:
    r, s = instruction[0], int(instruction[1:])
    current_dir = directions[(r, current_dir)]
    for step in range(s):
        current += current_dir
        if not done and current in visited:
            done = True
            print("Part 2: " + str(abs(current.real) + abs(current.imag)))
        if not done:
            visited.add(current)
    
print("Part 1: " + str(abs(current.real) + abs(current.imag)))

