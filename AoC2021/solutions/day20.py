def area(x, y):
    return [(i, j) for j in (y-1, y, y+1) for i in (x-1, x, x+1)]


with open("../inputs/20.txt") as f:
    rules = [rule == "#" for rule in next(f)]
    assert not (rules[0] and rules[-1])
    even_on = rules[0]

    image = f.read().strip().split("\n")
    n, m = len(image), len(image[0])
    image = {(i, j) for j in range(n) for i in range(m) if image[j][i] == "#"}

min_x, max_x, min_y, max_y = 0, m, 0, n
on, prev_on = True, True
for step in range(1, 51):
    on = not on if even_on else on
    new_image = set()

    min_x, max_x = min_x - 1, max_x + 1
    min_y, max_y = min_y - 1, max_y + 1
    for j in range (min_y, max_y):
        for i in range(min_x, max_x):
            rule = [
                    "01"[px in image if prev_on else px not in image]
                    for px in area(i, j)
            ]
            turn_on = rules[int("".join(rule), 2)]

            if (turn_on and on) or (not turn_on and not on):
                new_image.add((i, j))

    image = new_image
    prev_on = on

    if step in [2, 50]:
        print(f"Day 20 part {int(step == 50) + 1}: {len(image)}")
