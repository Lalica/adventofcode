with open('../inputs/05.txt') as f:
    data = [line.strip() for line in f]


def binary(rules, low, high, low_rule):
    for r in rules:
        half = int((high - low)/2) + low
        if r == low_rule:
            high = half
        else:
            low = half + 1
    return low


highest = 0
seats = [False] * 1024
for seat in data:
    row_rules = seat[:7]
    col_rules = seat[7:]
    row = binary(row_rules, 0, 127, 'F')
    col = binary(col_rules, 0, 7, 'L')

    seat_id = row * 8 + col
    highest = max(highest, seat_id)
    seats[seat_id] = True
print(f'Day 5 part 1: {highest}')

for i in range(1, len(seats)):
    if seats[i-1] and seats[i+1] and not seats[i]:
        print(f'Day 5 part 2: {i}')
        break

# another solution
# seats = sorted([int(''.join('01'[c in 'BR'] for c in line), base=2) for line in data])
# print(f'Day 5 part 1: {seats[-1]}')

# for i in range(1, len(seats)):
#     if seats[i-1]+1 != seats[i]:
#         print(f'Day 5 part 2: {seats[i-1]+1}')
#         break
