from collections import defaultdict


def neighbors(current):
    return [current + i + j * 1j for j in range(-1, 2) for i in range(-1, 2)]


with open("../inputs/20.txt") as f:
    rules, image = f.read().strip().split("\n\n")
    rules = [rule == "#" for rule in rules]
    image_list = image.split("\n")
    image = defaultdict(bool)

    for j in range(len(image_list)):
        for i in range(len(image_list[0])):
            image[i + j * 1j] = image_list[j][i] == "#"

min_x = int(min(x.real for x in image))
max_x = int(max(x.real for x in image))
min_y = int(min(x.imag for x in image))
max_y = int(max(x.imag for x in image))

for step in range(1, 51):
    new_image = defaultdict(lambda: step % 2 == 0)
    min_x = int(min(x.real - 1 for x in image))
    max_x = int(max(x.real + 1 for x in image))
    min_y = int(min(x.imag - 1 for x in image))
    max_y = int(max(x.imag + 1 for x in image))

    for j in range (min_y, max_y + 1):
        for i in range(min_x, max_x + 1):
            new_image[i + j * 1j] = rules[int("".join("01"[image[nbr]] for nbr in neighbors(i + j * 1j)), 2)]
    image = new_image

    if step in [2, 50]:
        print(f"Day 20 part {int(step == 50) + 1}: {sum(image.values())}")
