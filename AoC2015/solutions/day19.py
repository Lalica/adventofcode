import re


def findall(pattern, string):
    start_index = string.find(pattern)
    while start_index != -1:
        yield start_index
        start_index = string.find(pattern, start_index + 1)


def replace_all(molecule, x, y):
    indexes = findall(x, molecule)

    new_molecules = set()
    for index in indexes:
        new_molecules.add(molecule[:index] + y + molecule[index + len(x):])

    return new_molecules


with open("../inputs/19.txt") as f:
    formulas, molecule = f.read().split('\n\n')
    formulas = [formula.split(" => ") for formula in formulas.split('\n')]

results = set()
for formula in formulas:
    results = results.union(replace_all(molecule, formula[0], formula[1]))

print(f"Day 19 part 1: {len(results)}")

molecule = molecule.replace("Rn", "(")
molecule = molecule.replace("Ar", ")")
molecule = molecule.replace("Y", ",")
molecule = re.sub(r"[A-Z][a-z]?", r"X", molecule)

num_transitions = molecule.count("X") - molecule.count(",") - 1

print(f"Day 19 part 2: {num_transitions}")
