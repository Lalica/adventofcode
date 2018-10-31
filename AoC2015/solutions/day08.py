from ast import literal_eval


with open("../inputs/08.txt") as f:
    input = f.read().strip().splitlines()

num, charsOfCode, num2 = 0, 0, 0
for i in input:
    num += len(literal_eval(i))
    charsOfCode += len(i)
    num2 += i.count("\"") + i.count("\\") + 2

print("Day 8 part 1: " + str(charsOfCode - num))
print("Day 8 part 1: " + str(num2))
