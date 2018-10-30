field1 = [[0 for i in range(1000)] for i in range(1000)]
field2 = [[0 for i in range(1000)] for i in range(1000)]


def change(fun, start, end):
    for i in range(int(start[0]), int(end[0])+1):
        for j in range(int(start[1]), int(end[1])+1):
            if fun == "on":
                field1[i][j] = 1
            elif fun == "off":
                field1[i][j] = 0
            else:
                field1[i][j] = not field1[i][j]
    return


def brightness(fun, start, end):
    for i in range(int(start[0]), int(end[0])+1):
        for j in range(int(start[1]), int(end[1])+1):
            if fun == "on":
                field2[i][j] += 1
            elif fun == "off" and field2[i][j] > 0:
                field2[i][j] -= 1
            elif fun == "toggle":
                field2[i][j] += 2
    return


with open("../inputs/06.txt") as f:
    input = f.read().strip().splitlines()

for i in input:
    row = i.split()
    function = row[-4]
    start, end = row[-3].split(','), row[-1].split(',')
    change(function, start, end)
    brightness(function, start, end)

print("Day 5 part 1: " + str(sum([sum(i) for i in field1])))
print("Day 5 part 2: " + str(sum([sum(i) for i in field2])))
