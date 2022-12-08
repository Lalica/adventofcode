from collections import defaultdict


def solve(recepies, alergens, ingredients):
    al_to_ing = defaultdict(set)
    solved = set()

    for alergen in alergens:
        al_to_ing[alergen] = set.intersection(
            *[ing for ing, al in recepies if alergen in al])

        if len(al_to_ing[alergen]) == 1:
            solved = solved.union(al_to_ing[alergen])

    while len(solved) != len(alergens):
        for alergen in al_to_ing:
            if len(al_to_ing[alergen]) == 1:
                continue

            al_to_ing[alergen] = al_to_ing[alergen].difference(solved)

            if len(al_to_ing[alergen]) == 1:
                solved = solved.union(al_to_ing[alergen])

    no_alg = ingredients.difference(set.union(*al_to_ing.values()))
    cnt = sum([len(recepie[0].intersection(no_alg)) for recepie in recepies])
    print(f'Day 21 part 1: {cnt}')

    part2 = ','.join([next(iter(al_to_ing[al])) for al in sorted(alergens)])
    print(f'Day 21 part 2: {part2}')


recepies = []
alergens, ingredients = set(), set()

with open('../inputs/21.txt') as f:
    for line in f.readlines():
        r_ingredients, r_alergens = line[:-2].split(' (contains ')
        r_ingredients = set(r_ingredients.split())
        r_alergens = set(r_alergens.split(', '))

        ingredients = ingredients.union(r_ingredients)
        alergens = alergens.union(r_alergens)

        recepies.append((r_ingredients, r_alergens))

solve(recepies, alergens, ingredients)
