with open('../inputs/02.txt') as f:
    data = [line.split(': ') for line in f]

valid_part_1 = 0
valid_part_2 = 0
for rule, password in data:
    minmax, letter = rule.split(' ')
    a, b = map(int, minmax.split('-'))

    occurrences = sum(1 for p in password if p == letter)
    if occurrences >= a and occurrences <= b:
        valid_part_1 += 1

    if (password[a-1] == letter and password[b-1] != letter) or \
       (password[a-1] != letter and password[b-1] == letter):
        valid_part_2 += 1

print(f'Day 2 part 1: {valid_part_1}')
print(f'Day 2 part 2: {valid_part_2}')
