from itertools import product, combinations
from collections import defaultdict


def powerset(s):
    return [frozenset(c) for r in range(len(s) + 1) for c in combinations(s, r)]


def shortest_paths(graph, vents, start):
    nodes = graph.keys()
    dist = defaultdict(lambda: float("inf"))

    for s in graph:
        for e in graph[s]:
            dist[(s, e)] = 1
    for s in nodes:
        dist[(s, s)] = 0

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]:
                    dist[(i, j)] = dist[(i, k)] + dist[(k, j)]

    nodes = vents | {start}
    return {s: [(e, dist[(s, e)]) for e in nodes if e != s] for s in nodes}



def calculate_pressures(start_time, graph):
    scores = dict()
    subsets = powerset(set(graph.keys()))

    for node in graph:
        for opened in subsets:
            scores[(0, node, opened)] = 0

    for time in range(1, start_time + 1):
        for node in graph:
            for opened in subsets:
                best_score = 0
                for nbr, dist in graph[node]:
                    time_left = time - dist
                    if time_left >= 0:
                        best_score = max(best_score, scores[(time_left, nbr, opened)])

                    if nbr not in opened and time_left >= 1:
                        score = pressures[nbr] * (time_left - 1) + \
                                scores[(time_left - 1, nbr, opened | frozenset({nbr}))]
                        best_score = max(best_score, score)

                scores[(time, node, opened)] = best_score

    return scores


def combine(time, pos, scores, vents):
    return max(
            scores[(time, pos, subset)] +
            scores[(time, pos, vents - subset)]
            for subset in powerset(vents))


with open("../inputs/16.txt") as f:
    graph = dict()
    start = "AA"
    pressures = {start: 0}
    for line in f:
        line = line.split()
        node = line[1]
        pressure = int(line[4].split("=")[1][:-1])
        graph[node]= "".join(line[9:]).split(",")
        if pressure:
            pressures[node] = pressure

vents = frozenset(pressures.keys())
graph = shortest_paths(graph, vents, start) 
scores = calculate_pressures(30, graph)

part1 = scores[30, start, frozenset()]
print(f'Day 16 part 1: {part1}')

part2 = combine(26, start, scores, vents)
print(f'Day 16 part 2: {part2}')
