import re
from collections import defaultdict

directions = {
    'e': +1 + 0j,
    'ne': +1 - 1j,
    'nw': +0 - 1j,
    'w': -1 + 0j,
    'sw': -1 + 1j,
    'se': +0 + 1j
}
neighbours = ['e', 'ne', 'nw', 'w', 'sw', 'se']


def hex_neighbor(hex, direction):
    dir = directions[direction]
    return hex + dir


def flip(hex, grid, new_grid):
    num_neighbours = sum([grid[hex_neighbor(hex, n)] for n in neighbours])

    if grid[hex] and (num_neighbours == 0 or num_neighbours > 2):
        new_grid[hex] = False  # white
    elif not grid[hex] and num_neighbours == 2:
        new_grid[hex] = True  # black
    else:
        new_grid[hex] = grid[hex]


def touch_neighbours(grid):
    hexes = list(grid.keys())
    for h in hexes:
        for n in neighbours:
            grid[hex_neighbor(h, n)] = grid[hex_neighbor(h, n)]


def solve(rules, grid, days):
    for rule in rules:
        direction = sum(directions[r] for r in rule)
        grid[direction] = not grid[direction]

    print(f'Day 24 part 1: {sum(grid.values())}')

    for _ in range(days):
        new_grid = defaultdict(bool)
        touch_neighbours(grid)

        hexes = list(grid.keys())
        for h in hexes:
            flip(h, grid, new_grid)

        grid = new_grid

    print(f'Day 24 part 2: {sum(grid.values())}')


with open('../inputs/24.txt') as f:
    rules = [re.findall('e|w|ne|nw|se|sw', line) for line in f]

grid = defaultdict(bool)  # white = False
days = 100
solve(rules, grid, days)
