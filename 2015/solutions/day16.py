stats = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}
gt_stats = {"cats", "trees"}
lt_stats = {"pomeranians", "goldfish"}
eq_stats = set(stats.keys()) - gt_stats - lt_stats

sues = dict()
with open("../inputs/16.txt") as f:
    for line in f:
        sue_end = line.index(":")
        sue = int(line[4: sue_end])

        rest = [kv.split(": ") for kv in line[sue_end + 2:].split(", ")]
        sues[sue] = {k: int(v) for k, v in rest}

remaining_sues1 = list(range(1, len(sues) + 1))
remaining_sues2 = list(range(1, len(sues) + 1))
for stat in stats:
    valid_sues1 = []
    valid_sues2 = []

    for sue in remaining_sues1:
        if stat not in sues[sue] or stats[stat] == sues[sue][stat]:
            valid_sues1.append(sue)

    for sue in remaining_sues2:
        if (
            stat not in sues[sue]
            or (stat in lt_stats and sues[sue][stat] < stats[stat])
            or (stat in gt_stats and sues[sue][stat] > stats[stat])
            or (stat in eq_stats and stats[stat] == sues[sue][stat])
        ):
            valid_sues2.append(sue)

    remaining_sues2 = valid_sues2
    remaining_sues1 = valid_sues1

print(f"Day 15 part 1: {remaining_sues1[0]}")
print(f"Day 15 part 2: {remaining_sues2[0]}")
