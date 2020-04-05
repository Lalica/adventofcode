import re

clay, still_water, water, source = set(), set(), set(), set()


def move(x, y, step):
    while (y, x) not in clay and ((y + 1, x) in clay or (y + 1, x) in still_water):
        x += step
    return (y, x) in clay, x


def drip():
    y, x = source.pop()
    water.add((y, x))
    while (y+1, x) not in clay and (y+1, x) not in still_water:
        if y+1 > y_max or ((y+1, x) in water and (y+1, x) not in still_water):
            return
        water.add((y+1, x))
        y += 1

    fl = fr = True
    while fl and fr:
        fl, xl = move(x, y, -1)
        fr, xr = move(x, y, 1)

        for i in range(xl + 1, xr):
            water.add((y, i))
            if fl and fr:
                still_water.add((y, i))

        if not fl:
            source.add((y, xl))
        if not fr:
            source.add((y, xr))
        y -= 1


with open('../inputs/17.txt') as f:
    for l in f:
        m, n, k = map(int, re.findall(r'\d+', l))
        for i in range(n, k + 1):
            clay.add((i, m) if l[0] == 'x' else (m, i))

y_min = min(y for y, x in clay)
y_max = max(y for y, x in clay)

source.add((y_min, 500))
while len(source):
    drip()

print('Day 17 part 1: ' +  str(len(water)))
print('Day 17 part 2: ' +  str(len(still_water)))

with open('test.txt', 'w+') as f:
    f.write(''.join(['.'] * (500 - 350)) + '+' + ''.join(['.'] * (700 - 501)) + '\n')
    for i in range(y_max + 1):
        for j in range(350, 700):
            f.write('#' if (i, j) in clay else '~' if (i, j) in still_water else '|' if (i, j) in water else '.')
        f.write('\n')
