from math import ceil


weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
armours = [[0, 0, 0], [13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
rings = [[0, 0, 0], [20, 0, 1], [25, 1, 0], [40, 0, 2], [50, 2, 0], [80, 0, 3], [100, 3, 0]]


def win_condition():
    return (
            ceil(boss[0] / max(1, me[1] - boss[2]))
            <= ceil(me[0] / max(1, boss[1] - me[2]))
    )


def remove_item(item, me, gold):
    me[1] -= item[1]
    me[2] -= item[2]
    return gold - item[0]


def try_item(item, me, gold):
    global min_gold, max_gold

    gold += item[0]
    me[1] += item[1]
    me[2] += item[2]

    if win_condition():
        min_gold = min(min_gold, gold)
    else:
        max_gold = max(max_gold, gold)

    return gold


with open("../inputs/21.txt") as f:
    boss = [int(line.split()[-1]) for line in f]
    me = [100, 0, 0]

min_gold, max_gold = float("inf"), 0
gold = 0
for w in weapons:
    gold = try_item(w, me, gold)

    for a in armours:
        gold = try_item(a, me, gold)

        for r1 in rings:
            gold = try_item(r1, me, gold)

            for r2 in rings:
                if r1 != r2:
                    gold = try_item(r2, me, gold)
                    gold = remove_item(r2, me, gold)
            gold = remove_item(r1, me, gold)
        gold = remove_item(a, me, gold)
    gold = remove_item(w, me, gold)

print(min_gold)
print(max_gold)
