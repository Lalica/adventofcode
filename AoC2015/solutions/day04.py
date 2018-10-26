import hashlib

with open("../inputs/04.txt") as f:
    input = f.read().strip()

num = 0
while not hashlib.md5(input + str(num)).hexdigest().startswith('00000'):
    num += 1
print("Day 4 part 1: " + str(num))

while not hashlib.md5(input + str(num)).hexdigest().startswith('000000'):
    num += 1
print("Day 4 part 2: " + str(num))
