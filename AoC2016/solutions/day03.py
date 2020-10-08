from itertools import zip_longest

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

def check_triangle(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a

with open("../inputs/03.txt") as f:
    data = f.read().strip().splitlines()

counter1, counter2 = 0, 0
for line in data:
    a, b, c = list(map(int, line.split()))
    if check_triangle(a, b, c):
        counter1 += 1

for line1, line2, line3 in grouper(3, data, 0):
    a1, a2, a3 = list(map(int, line1.split()))
    b1, b2, b3 = list(map(int, line2.split()))
    c1, c2, c3 = list(map(int, line3.split()))
    if check_triangle(a1, b1, c1):
        counter2 += 1
    if check_triangle(a2, b2, c2):
        counter2 += 1
    if check_triangle(a3, b3, c3):
        counter2 += 1

print("Day 3 part 1: " + str(counter1))
print("Day 3 part 2: " + str(counter2))

