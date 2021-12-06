def rules(pwd):
    rule1, rule2 = False, True

    pairs, seen = 0, ""
    for i in range(len(pwd)):
        if i > 1 and pwd[i - 2] + 2 == pwd[i] and pwd[i - 1] + 1 == pwd[i]:
            rule1 = True

        if pwd[i] in not_allowed:
            rule2 = False

        if i > 0 and pwd[i - 1] == pwd[i] and pwd[i] != seen:
            seen = pwd[i]
            pairs += 1

    return rule1 and rule2 and pairs >= 2


def next_pwd(pwd):
    for i in range(len(pwd) - 1, -1, -1):
        pwd[i] = (pwd[i] + 1) % 26
        if pwd[i] != 0:
            break
    return pwd


with open("../inputs/11.txt") as f:
    pwd = [ord(letter) - 97 for letter in f.read().strip()]
not_allowed = [8, 11, 14]  # i, l, o

part = 1
while part < 3:
    pwd = next_pwd(pwd)
    if rules(pwd):
        part += 1
        str_pwd = "".join(chr(p + 97) for p in pwd)
        print(f"Day 11 part {part}: {str_pwd}")
