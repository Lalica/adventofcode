def get_ancestors(planet):
    if planet not in orbits:
        return []

    return get_ancestors(orbits[planet]) + [orbits[planet]]


with open('../inputs/06.txt') as f:
    orbits = {}
    for line in f:
        a, b = line[:-1].split(")")
        orbits[b] = a

part1 = sum(len(get_ancestors(planet)) for planet in orbits)
print(f'Day 6 part 1: {part1}')

you = get_ancestors(orbits["YOU"])
san = get_ancestors(orbits["SAN"])
i = 0
while i < len(you) and i < len(san) and you[i] == san[i]:
    i += 1

part2 = len(you) - i + len(san) - i + 2
print(f'Day 6 part 2: {part2}')
