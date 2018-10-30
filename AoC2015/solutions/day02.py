def find_smallest(w, l, h):
    array = [h, l, w]
    array.sort()
    return array[0], array[1]


with open("../inputs/02.txt") as f:
    input = f.read().strip().splitlines()

total, ribbon = 0, 0
for line in input:
    h, l, w = int(line.split('x')[0]), int(line.split('x')[1]), int(line.split('x')[2])
    smallest = find_smallest(w, l, h)
    total += 2*l*w + 2*w*h + 2*h*l + smallest[0]*smallest[1]
    ribbon += 2*(smallest[0]) + 2*(smallest[1]) + h*l*w

print("Day 2 part 1: " + str(total))
print("Day 2 part 2: " + str(ribbon))
