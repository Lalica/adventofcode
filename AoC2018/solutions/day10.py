from re import findall
from collections import defaultdict


data = [map(int, findall(r'-*\d+', i)) for i in (open("../inputs/10.txt").readlines())]
seconds = 0

while True:
    seconds += 1
    stars = defaultdict(lambda: ' ')
    minx, maxx, miny, maxy = data[0][0], data[0][0], data[0][1], data[0][1]
    for i in data:
        i[0], i[1] = i[0] + i[2], i[1] + i[3]
        stars[(i[0], i[1])] = '#'
        minx = min(minx, i[0])
        maxx = max(maxx, i[0])
        miny = min(miny, i[1])
        maxy = max(maxy, i[1])

    if seconds > 1 and abs(maxx - minx) > abs(prev_maxx - prev_minx):
        for j in range(prev_miny, prev_maxy + 1):
            s = ""
            for i in range(prev_minx, prev_maxx + 1):
                s += old_stars[(i, j)]
            print(s)
        print(seconds - 1)
        exit(1)
    prev_minx, prev_maxx, prev_miny, prev_maxy = minx, maxx, miny, maxy
    old_stars = stars.copy()
