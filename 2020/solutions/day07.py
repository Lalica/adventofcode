with open('../inputs/07.txt') as f:
    bags = dict()
    for line in f:
        k, v = line.strip()[:-1].split(' contain ')
        key = k.replace(' bags', '')
        contains = []
        for b in v.split(', '):
            bi = b.split(' ')
            if bi[0] != 'no':
                contains.append((int(bi[0]), ' '.join(bi[1:-1])))
        bags[key] = contains
visited = set()


def find_shiny_gold(bag, bags):
    for b in bags:
        if bag in [o[1] for o in bags[b]]:
            visited.add(b)
            find_shiny_gold(b, bags)


def count_bags(bag, bags):
    sum_cnt = 0
    for b in bags[bag]:
        sum_cnt += b[0] + b[0] * count_bags(b[1], bags)
    return sum_cnt


find_shiny_gold('shiny gold', bags)
part2 = count_bags('shiny gold', bags)
print(f'Day 7 part 1: {len(visited)}')
print(f'Day 7 part 2: {part2}')
