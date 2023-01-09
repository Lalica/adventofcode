import re
from collections import defaultdict
from itertools import product, combinations
from functools import cache


@cache
def open_valves(time, v, closed):
    if time <= 0:
        return 0

    best_score = 0
    for u in closed:
        time_left = time - dist[v, u] - 1
        score = pressures[u] * time_left + open_valves(time_left, u, closed - {u})
        best_score = max(best_score, score)

    return best_score


def powerset(s):
    return [frozenset(c) for r in range(len(s) + 1) for c in combinations(s, r)]


def combine(time, pos, valves):
    return max(
            open_valves(time, pos, subset) +
            open_valves(time, pos, valves - subset)
            for subset in powerset(valves))


with open("../inputs/16.txt") as f:
    pressures = dict()
    V = set()
    dist = defaultdict(lambda: float("inf"))

    r = r'Valve (\w+) .*=(\d*); .* valves? (.*)'
    for v, pressure, nbrs in re.findall(r, f.read()):
        V.add(v)
        if pressure != '0':
            pressures[v] = int(pressure)
        for u in nbrs.split(', '):
            dist[v, u] = 1

for k, i, j in product(V, V, V):
    dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])
valves = frozenset(pressures.keys())

part1 = open_valves(30, 'AA', valves)
print(f'Day 16 part 1: {part1}')

part2 = combine(26, 'AA', valves)
print(f'Day 16 part 2: {part2}')
