import re

with open("../inputs/05.txt") as f:
    input = f.read().strip().splitlines()

num = 0
for i in input:
    if re.match(".*([aeiou].*){3}", i) and re.match("^((?!ab|cd|xy|pq).)*$", i) and re.match(".*(.)\\1", i):
        num += 1
print("Day 5 part 1: " + str(num))

num = 0
for i in input:
    if re.match(".*((.)(.)).*\\1", i) and re.match(".*(.).\\1", i):
        num += 1
print("Day 5 part 2: " + str(num))
