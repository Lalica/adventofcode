from string import ascii_uppercase
from re import sub


def minimize(s):
    i = 0
    while i < len(s) - 1:
        if abs(ord(s[i]) - ord(s[i + 1])) == 32:
            s = s[:i] + s[i + 2:]
            i = i - 2 if i > 0 else -1
        i += 1
    return s


data = minimize(open("../inputs/05.txt").read().strip())

print("Day 5 part 1: " + str(len(data)))
print("Day 5 part 2: " + str(min(len(minimize(sub('[' + c + c.lower() + ']', '', data))) for c in ascii_uppercase)))
