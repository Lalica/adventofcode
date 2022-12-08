def halves(container):
    half = len(container)//2
    return container[:half], container[half:]


def priority(c):
    return ord(c) - [ord('A') - 27, ord('a') - 1][c.islower()]


def groups_of_3(items):
    for g in range(0, len(items), 3):
        yield items[g:g+3]


with open("../inputs/03.txt") as f:
    rucksacks = f.read().splitlines()

conpartments = [tuple(map(set, halves(r))) for r in rucksacks]
shared_items = [next(iter(c1 & c2)) for c1, c2 in conpartments]
part1 = sum(priority(item) for item in shared_items)
print(f'Day 3 part 1: {part1}')

badges = [next(iter(set.intersection(*map(set, g)))) for g in groups_of_3(rucksacks)]
part2 = sum(priority(badge) for badge in badges)
print(f'Day 3 part 2: {part2}')
