from collections import defaultdict


serial = int(open("../inputs/11.txt").read())
grid_sums, partial_sums = {}, defaultdict(int)

power_level = lambda x, y: ((((x + 10) * y + serial) * (x + 10)) // 10 ** 2 % 10) - 5
# I(x,y)=i(x,y)+I(x,y-1)+I(x-1,y)-I(x-1,y-1)
calculate_ps = lambda x, y: (power_level(x + 1, y + 1)
                             + partial_sums[x, y-1] + partial_sums[x-1, y] - partial_sums[x-1, y-1])

for j in range(300):
    for i in range(300):
        partial_sums[(i, j)] = calculate_ps(i, j)

for size in range(2, 300):
    for j in range(size-1, 300):
        for i in range(size-1, 300):
            gp = partial_sums[(i, j)] + partial_sums[(i-size, j-size)] \
                 - partial_sums[(i-size, j)] - partial_sums[(i, j-size)]
            grid_sums[gp] = (i-size+2, j-size+2, size)
    if size == 3:
        x3, y3, s3 = map(str, grid_sums[max(grid_sums)])
        print("Day 11 part 1: " + x3 + "," + y3)

print("Day 11 part 2: %d,%d,%d" % grid_sums[max(grid_sums)])
