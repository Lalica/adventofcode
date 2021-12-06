import re
from functools import reduce


with open("../inputs/15.txt") as f:
    ingredients = [list(map(int, re.findall(r"-?\d+", line))) for line in f]

max_score = 0
max_calorie_score = 0
for i in range(101):
    for j in range(101 - i):
        for k in range(101 - i - j):
            scores = [
                max(
                    0,
                    sum(
                        value * quantity
                        for value, quantity in
                        zip(nums, [i, j, k, 100 - i - j - k])
                    ),
                )
                for nums in zip(*ingredients)
            ]
            score = reduce((lambda x, y: x * y), scores[:-1])

            max_score = max(max_score, score)
            if scores[-1] == 500:
                max_calorie_score = max(max_calorie_score, score)

print(f"Day 15 part 1: {max_score}")
print(f"Day 15 part 2: {max_calorie_score}")
