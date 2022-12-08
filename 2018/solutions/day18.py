def count(type, y, x):
    cnt = 0
    for i in [y-1, y, y+1]:
        for j in [x-1, x, x+1]:
            if 0 <= i < 50 and 0 <= j < 50 and (i != y or j != x):
                cnt += 1 if field[i][j] == type else 0
    return cnt


with open('../inputs/18.txt') as f:
    field = [list(l)[:-1] for l in f]

tmp = [x[:] for x in [['.'] * 50] * 50]
results = []

for time in range(1, 1000000001):
    for i in range(50):
        for j in range(50):
            if field[i][j] == '#':
                tmp[i][j] = '#' if count('#', i, j) > 0 and count('|', i, j) > 0 else '.'
            elif field[i][j] == '|':
                tmp[i][j] = '#' if count('#', i, j) > 2 else '|'
            else:
                tmp[i][j] = '|' if count('|', i, j) > 2 else '.'
    field = [x[:] for x in tmp]

    if time == 10:
        lumberyards = sum(x == '#' for y in field for x in y)
        wooded_acres = sum(x == '|' for y in field for x in y)
        print('Day 18 part 1: ' + str(lumberyards*wooded_acres))

    if time >= 1000:
        lumberyards = sum(x == '#' for y in field for x in y)
        wooded_acres = sum(x == '|' for y in field for x in y)
        if lumberyards * wooded_acres in results:
            t = results.index(lumberyards * wooded_acres)
            period = (time - 1000) - (t + 1)
            t += 1000000000 % period - (t + 1) % period
            print('Day 18 part 2: ' + str(results[t]))
            break
        results.append(lumberyards * wooded_acres)
