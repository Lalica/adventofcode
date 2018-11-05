def replace(m, x, y, s):
    index = m.find(x, s)
    if index == -1:
        return
    results.add(m[:index] + y + m[index + len(x):])
    replace(m, x, y, index + 1)


with open("../inputs/19.txt") as f:
    input = [i.split(" => ") for i in f.read().strip().splitlines()]
    molecule = input.pop(-1)[0]
    input.pop(-1)

results = set()
for i in input:
    replace(molecule, i[0], i[1], 0)

print("Day 19 part 1: " + str(len(results)))

results, steps, newResults, flag = set(), 0, set(), 0
newResults.add(molecule)

while 1:
    for r in newResults:
        for i in input:
            replace(r, i[1], i[0], 0)
        if "e" in results:
            flag = 1
            break
    newResults = results - newResults
    steps += 1
    if flag:
        break

print("Day 19 part 2: " + str(steps))
