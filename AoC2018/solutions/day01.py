data = [int(x) for x in open("../inputs/01.txt").read().strip().splitlines()]

print("Day 1 part 1: " + str(sum(i for i in data)))

occurrence, s, f = set(), 0, False
occurrence.add(0)
while not f:
    for i in range(len(data)):
        s += data[i]
        if s in occurrence:
            f = True
            break
        occurrence.add(s)

print("Day 1 part 2: " + str(s))

