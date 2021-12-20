from collections import defaultdict


def area(x, y):
    return [(i, j) for j in [y-1, y, y+1] for i in [x-1, x, x+1]]


with open("../inputs/20.txt") as f:
    rules = [rule == "#" for rule in next(f)]
    assert not (rules[0] and rules[-1])
    even_on = rules[0]

    image_list = f.read().strip().split("\n")
    image = defaultdict(bool)
    n, m = len(image_list), len(image_list[0])
    for j in range(n):
        for i in range(m):
            image[(i, j)] = image_list[j][i] == "#"

min_x, max_x, min_y, max_y = 0, m, 0, n
for step in range(1, 51):
    if even_on:
        new_image = defaultdict(lambda: step % 2 == 0)
    else:
        new_image = defaultdict(bool)

    min_x, max_x = min_x - 1, max_x + 1
    min_y, max_y = min_y - 1, max_y + 1
    for j in range (min_y, max_y):
        for i in range(min_x, max_x):
            rule = ["01"[image[px]] for px in area(i, j)]
            new_image[(i, j)] = rules[int("".join(rule), 2)]

    image = new_image

    if step in [2, 50]:
        print(f"Day 20 part {int(step == 50) + 1}: {sum(image.values())}")
