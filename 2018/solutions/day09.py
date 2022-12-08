from re import findall
from collections import defaultdict, deque


def game(nbrp, marbles):
    # circle, current, players = [0], 0, defaultdict(int)
    circle, players = deque([0]), defaultdict(int)
    for i in range(1, marbles + 1):
        if not i % 23:
            # current = (current - 7 + len(circle)) % len(circle)
            circle.rotate(7)
            players[i % nbrp] += i + circle.pop()  # circle.pop(current)
            circle.rotate(-1)
            continue
        # current = (current + 2) % len(circle)
        # current = current if current else len(circle)
        # circle.insert(current, i)
        circle.rotate(-1)
        circle.append(i)

    return max(players.values())


p, m = map(int, findall(r'\d+', open("../inputs/09.txt").read()))

print("Day 9 part 1: " + str(game(p, m)))
print("Day 9 part 2: " + str(game(p, m * 100)))
