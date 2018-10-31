with open("../inputs/08.txt") as f:
    input = f.read().strip().splitlines()

print("Day 8 part 1: " + str(sum(len(i) - len(i.decode('unicode_escape')) + 2 for i in input)))
print("Day 8 part 2: " + str(sum(i.count("\"") + i.count("\\") + 2 for i in input)))
