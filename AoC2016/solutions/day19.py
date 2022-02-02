with open("../inputs/19.txt") as f:
    n = int(f.read())

pow2 = 1
while pow2 < n:
    pow2 *= 2
pow2 //= 2

index = (n - pow2) * 2 + 1
print(f"Day 19 part 1: {index}")

pow3 = 1
while pow3 < n:
    pow3 *= 3
pow3 //= 3

if n - pow3 <= pow3:
    index = n - pow3
else:
    index = (n - 2 * pow3) // 2 + 1
print(f"Day 19 part 2: {index}")
