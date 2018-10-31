with open("../inputs/03.txt") as f:
    input = f.read().strip()

step = len(input)
move = {'^': -step, 'v': step, '<': -1, '>': 1}
current1, houses1, current2, houses2 = [0], set(), [0, 0], set()
houses1.add(current1[0])
houses2.add(current1[0])

for i in range(len(input)):
    # part 1
    current1[0] += move[input[i]]
    houses1.add(current1[0])
    # part 2
    current2[i % 2] += move[input[i]]
    houses2.add(current2[i % 2])

print("Day 3 part 1: " + str(len(houses1)))
print("Day 3 part 2: " + str(len(houses2)))
