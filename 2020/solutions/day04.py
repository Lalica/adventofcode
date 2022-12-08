import re

with open('../inputs/04.txt') as f:
    passports = list(line for line in f.read().strip().split('\n\n'))
    data = list(dict(field.split(':')
                     for field in line.replace('\n', ' ').split())
                for line in passports)

present = 0
valid = 0
good = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
for person in data:
    if all(g in person for g in good):
        present += 1
        if 1920 <= int(person['byr']) <= 2002 and \
           2010 <= int(person['iyr']) <= 2020 and \
           2020 <= int(person['eyr']) <= 2030 and \
           (('cm' in person['hgt'] and 150 <= int(person['hgt'][:-2]) <= 193) or
            ('in' in person['hgt'] and 59 <= int(person['hgt'][:-2]) <= 76)) and \
           re.match('^#[0-9a-f]{6}$', person['hcl']) and \
           person['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
           re.match('^[0-9]{9}$', person['pid']):
            valid += 1

print(f'Day 4 part 1: {present}')
print(f'Day 4 part 2: {valid}')
