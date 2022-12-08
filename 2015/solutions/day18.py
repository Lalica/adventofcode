from collections import defaultdict


def get_neighbours(num):
    return [
        num - 1,
        num + 1,
        num + 1j,
        num - 1j,
        num - 1 - 1j,
        num - 1 + 1j,
        num + 1 - 1j,
        num + 1 + 1j,
    ]


def play_game(lights, num_days, always_on):
    for _ in range(num_days):
        new_lights = lights.copy()
        for i in range(100):
            for j in range(100):
                if i + 1j * j in always_on:
                    continue

                neighbours = sum(lights[n] for n in get_neighbours(i + 1j * j))

                if lights[i + 1j * j] and neighbours not in [2, 3]:
                    new_lights[i + 1j * j] = False

                if not lights[i + 1j * j] and neighbours == 3:
                    new_lights[i + 1j * j] = True

        lights = new_lights

    return lights


initial_lights = defaultdict(bool)
with open("../inputs/18.txt") as f:
    i = 0
    for line in f:
        for j in range(len(line) - 1):
            initial_lights[i + 1j * j] = line[j] == "#"
        i += 1

lights = initial_lights.copy()
lights = play_game(lights, 100, [])
print(f"Day 18 part 1: {sum(lights.values())}")

lights = initial_lights.copy()
lights = play_game(lights, 100, [0, 99j, 99, 99 + 99j])
print(f"Day 18 part 2: {sum(lights.values())}")
