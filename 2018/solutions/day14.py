num = open("../inputs/14.txt").read().strip()
f, s = 0, 1
recipes = [3, 7]

while num not in "".join(map(str, recipes[-len(num)-1:])):
    new_rec = recipes[f] + recipes[s]
    if new_rec >= 10:
        recipes.append(new_rec // 10)
    recipes.append(new_rec % 10)
    f = (f + recipes[f] + 1) % len(recipes)
    s = (s + recipes[s] + 1) % len(recipes)

print("Day 14 part 1: " + "".join(map(str, recipes[int(num):int(num) + 10])))
print("Day 14 part 2: " + str("".join(map(str, recipes)).index(num)))
