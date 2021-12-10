with open("../inputs/10.txt") as f:
    lines = f.readlines()

complement = {")": "(", "}": "{", "]": "[", ">": "<"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4}

part1 = 0
part2 = []
for line in lines:
    stack = []
    for char in line.strip():
        if char in "({[<":
            stack.append(char)
        else:
            if not stack or complement[char] != stack[-1]:
                part1 += points[char]
                break
            stack.pop()
    else:
        score = 0
        for char in reversed(stack):
            score = score * 5 + points[char]
        part2.append(score)

print(f"Day 10 part 1: {part1}")
print(f"Day 10 part 2: {sorted(part2)[len(part2)//2]}")
