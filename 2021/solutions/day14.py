from collections import Counter


with open("../inputs/14.txt") as f:
    molecule = next(f).strip()
    next(f)
    rules = dict(line.strip().split(" -> ") for line in f)

pairs = Counter([molecule[i: i + 2] for i in range(len(molecule) - 1)])

for step in range(1, 41):
    new_pairs = Counter()
    for pair in pairs:
        new_pairs[pair[0] + rules[pair]] += pairs[pair]
        new_pairs[rules[pair] + pair[1]] += pairs[pair]
    pairs = new_pairs

    if step in [10, 40]:
        letters = Counter()
        for pair in pairs:
            letters[pair[0]] += pairs[pair]
        letters[molecule[-1]] += 1

        most_common = letters.most_common()
        part = 1 if step == 10 else 2
        print(f"Day 14 part {part}: {most_common[0][1] - most_common[-1][1]}")
