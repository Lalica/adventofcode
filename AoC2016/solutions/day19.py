with open("../inputs/19.txt") as f:
    number = int(f.read())

pow2 = 1
while pow2 < number:
    pow2 *= 2
pow2 /= 2
index = (number - pow2) * 2 + 1

print(f"Day 19 part 1: {index}")

# used for finding pattern
#
# for i in range(1, 30):
#     numbers = [*range(1, i+1)]
#     index = 0
#     while len(numbers) > 1:
#         to_pop = (index + len(numbers)//2) % len(numbers)
#         if to_pop < index:
#             index -= 1
#         numbers.pop(to_pop)
#         index = (index + 1) % len(numbers)
#    print(f"{i} {numbers[0]}")

pow3 = 1
while pow3 < number:
    pow3 *= 3
pow3 /= 3
dif = number - pow3
index = dif if dif <= pow3 else (pow3//2 + dif - pow3) * 2 + 1

print(f"Day 19 part 2: {index}")

