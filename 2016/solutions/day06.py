from collections import defaultdict, Counter

with open("../inputs/06.txt") as f:
    data = f.read().strip().splitlines()

columns = defaultdict(lambda: [])

for line in data:
    for i in range(len(line)):
        columns[i].append(line[i])

result1 = ""
result2 = ""
for c in columns:
    most_common = Counter(columns[c]).most_common()
    result1 += most_common[0][0] 
    result2 += most_common[-1][0]

print(f"Day 6 part 1: {result1}")
print(f"Day 6 part 2: {result2}")

