def drive():
    first_crash = (-1, -1)
    while len(cars) > 1:
        tick = []
        for j in range(len(track)):
            for i in range(len(track[j])):
                if (i, j) in cars and cars[(i, j)][0] not in tick:
                    tick.append(cars[(i, j)][0])
                    x, y = directions[cars[(i, j)][2]]
                    if (i + x, j + y) in cars:
                        if first_crash == (-1, -1):
                            first_crash = (i + x, j + y)
                        cars.pop((i + x, j + y))
                        cars.pop((i, j))
                        continue
                    next_step = track[j + y][i + x]
                    if next_step == '+':
                        cars[(i, j)][2] = (4 + cars[(i, j)][2] + cars[(i, j)][1]) % 4
                        cars[(i, j)][1] = (cars[(i, j)][1] + 2) % 3 - 1
                    elif next_step == '/':
                        cars[(i, j)][2] = (cars[(i, j)][2] + 1) % 2 + (2 if cars[(i, j)][2] > 1 else 0)
                    elif next_step == '\\':
                        cars[(i, j)][2] = (cars[(i, j)][2] + 1) % 2 + (2 if cars[(i, j)][2] < 2 else 0)
                    cars[(i + x, j + y)] = cars.pop((i, j))
    return first_crash, cars.keys()[0]


find_direction = {'^': 0, '>': 1, 'v': 2, '<': 3}
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

track = open("../inputs/13.txt").read().splitlines()
cars, car_id = {}, 'a'
for i in range(len(track)):
    for j in range(len(track[i])):
        if track[i][j] in '><^v':
            cars[(j, i)] = [car_id, -1, find_direction[track[i][j]]]
            n = '-' if track[i][j] in '<>' else '|'
            track[i] = track[i][:j] + n + track[i][j+1:]
            car_id = chr(ord(car_id) + 1)

part1, part2 = drive()
print("Day 13 part 1: %d,%d" % part1)
print("Day 13 part 2: %d,%d" % part2)
