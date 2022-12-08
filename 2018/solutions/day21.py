r5 = 65536
r4 = 10704114
first, last, r4s = 0, 0, set()
while True:
    r4 = ((((r5 & 255) + r4) & 16777215) * 65899) & 16777215
    if r5 >= 256:
        r5 //= 256
        continue
    if first == 0:
        first = r4
    if r4 in r4s:
        break
    r4s.add(r4)
    last = r4
    r5 = r4 | 65536
    r4 = 10704114

print('Day 21 part 1: ' + str(first))
print('Day 21 part 2: ' + str(last))
