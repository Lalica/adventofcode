import re


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def scan(sensor, Y):
    x, y, _, _ = sensor
    sensor_range = manhattan(*sensor)

    delta_y = abs(y - Y)
    if delta_y > sensor_range:
        return set()

    points = set()
    for dx in range(sensor_range - delta_y + 1):
        points.add((x + dx, Y))
        points.add((x - dx, Y))

    return points


def scan_line(scan_data, Y):
    occupied = {(x, y) for x, y, _, _ in scan_data}
    occupied |= {(x, y) for _, _, x, y in scan_data}

    scanned = set.union(*[scan(sd, Y) for sd in scan_data])
    scanned -= occupied

    return len(scanned)


def outer_ring(sensor):
    x, y, _, _ = sensor
    sensor_range = manhattan(*sensor)

    dots = set()
    delta_y = sensor_range + 1
    for delta_x in range(sensor_range + 1):
        for i in [x - delta_x, x + delta_x]:
            for j in [y - delta_y, y + delta_y]:
                dots.add((i, j))
        delta_y -= 1

    return dots


def outside_boundries(dot, lower, higher):
    x, y = dot
    return x < lower or y < lower or x > higher or y > higher


def in_range(dot, sensor):
    sx, sy, _, _ = sensor
    return manhattan(*dot, sx, sy) <= manhattan(*sensor)


def find_pos(scan_data, lower, higher):
    for sensor in scan_data:
        for dot in outer_ring(sensor):
            if outside_boundries(dot, lower, higher):
                continue

            if not any(in_range(dot, s) for s in scan_data):
                return dot


with open("../inputs/15.txt") as f:
    scan_data = [list(map(int, re.findall("-?\d+", line))) for line in f]

Y = 2000000
part1 = scan_line(scan_data, Y)
print(f'Day 15 part 1: {part1}')

lower, higher = 0, 4000000
bx, by = find_pos(scan_data, lower, higher)
part2 = bx * 4000000 + by
print(f'Day 15 part 2: {part2}')
