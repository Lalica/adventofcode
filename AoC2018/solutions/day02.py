from collections import Counter


data = open("../inputs/02.txt").read().strip().splitlines()

m, n = 0, 0
for i in data:
    v = Counter(i).values()
    if 2 in v:
        m += 1
    if 3 in v:
        n += 1

print("Day 2 part 1: " + str(m*n))

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        for k in range(len(data[i])):
            if data[i][:k] + data[i][k+1:] == data[j][:k] + data[j][k+1:]:
                print("Day 2 part 2: " + data[i][:k] + data[i][k+1:])
                exit(1)
