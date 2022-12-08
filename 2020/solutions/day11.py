from collections import defaultdict


with open('../inputs/11.txt') as f:
    tmp = [list(line.strip()) for line in f]
    m, n = len(tmp), len(tmp[0])
    initial_area = defaultdict(lambda: '.')
    for j in range(m):
        for i in range(n):
            initial_area[i+j*1j] = tmp[j][i]


def neighbours1(area, x):
    return [x-1, x-1-1j, x-1j, x+1-1j, x+1, x+1+1j, x+1j, x-1+1j]


def neighbours2(area, x):
    directions = neighbours1(area, 0)
    nbs = []
    for d in directions:
        step = 1
        s = x+step*d
        while area[s] == '.' and (0 <= s.real < n and 0 <= s.imag < m):
            step += 1
            s = x+step*d
        nbs.append(s)
    return nbs


def pass_time(limit, neighbours):
    area = initial_area.copy()
    while True:
        new_area = defaultdict(lambda: '.')
        changed = False
        for j in range(m):
            for i in range(n):
                x = i + j*1j
                new_area[x] = area[x]
                if area[x] == 'L':
                    n_occupied = any(area[nb] == '#' for nb in neighbours(area, x))
                    if not n_occupied:
                        changed = True
                        new_area[x] = '#'
                elif area[x] == '#':
                    cnt = sum(area[nb] == '#' for nb in neighbours(area, x))
                    if cnt >= limit:
                        changed = True
                        new_area[x] = 'L'
        if not changed:
            return area
        area = new_area


area1 = pass_time(4, neighbours1)
area2 = pass_time(5, neighbours2)
cnt_occupied1 = sum(area1[i+j*1j] == '#' for i in range(n) for j in range(m))
cnt_occupied2 = sum(area2[i+j*1j] == '#' for i in range(n) for j in range(m))
print(f'Day 11 part 1: {cnt_occupied1}')
print(f'Day 11 part 2: {cnt_occupied2}')
