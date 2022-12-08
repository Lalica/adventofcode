from itertools import chain, permutations

# works only cuz num of cities is <10 and all cities are connected to each other hehe
with open('../inputs/9.txt') as f:
    edges = {frozenset(x.split(' to ')): int(y) for x, y in map(lambda l: l.split(' = '), f)}
    cities = set(chain(*edges))
    all_sums = [sum(edges[frozenset((p[i], p[i+1]))] for i in range(len(p)-1)) for p in permutations(cities)]
    print('Day 9 part 1: ' + str(min(all_sums)))
    print('Day 9 part 2: ' + str(max(all_sums)))
