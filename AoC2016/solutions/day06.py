moves = {"D": lambda x: 0 if x == 7 or x == 8 or x == 9 else 3,
         "U": lambda x: 0 if x == 1 or x == 2 or x == 3 else -3,
         "R": lambda x: 0 if x == 3 or x == 6 or x == 9 else 1,
         "L": lambda x: 0 if x == 1 or x == 4 or x == 7 else -1}

keypad = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, "A", "B", "C", 0], [0, 0, "D", 0, 0]]
moves2 = {"D": lambda x, y: (1, 0) if x < 4 else (0, 0),
          "U": lambda x, y: (-1, 0) if x > 0 else (0, 0),
          "R": lambda x, y: (0, 1) if y < 4 else (0, 0),
          "L": lambda x, y: (0, -1) if y > 0 else (0, 0)}

with open("../inputs/06.txt") as f:
    input = f.read().strip().splitlines()

current, code = 5, ""
for i in input:
    for j in i:
        current = current + moves[j](current)
    code += str(current)

print("Day 2 part 1: " + code)

current, code = (2, 0), ""
for i in input:
    for j in i:
        n = moves2[j](current[0], current[1])
        temp = (current[0] + n[0], current[1] + n[1])
        current = temp if keypad[temp[0]][temp[1]] != 0 else current
    code += str(keypad[current[0]][current[1]])

print("Day 2 part 2: " + code)
