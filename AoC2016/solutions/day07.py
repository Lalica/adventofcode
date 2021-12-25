def abba(string):
    for i in range(len(string)-3):
        a = string[i]
        b = string[i+1]
        b_ = string[i+2]
        a_ = string[i+3]
        if a == a_ and b == b_ and a != b:
            return True

    return False


def aba(string):
    babs = []
    for i in range(len(string)-2):
        a = string[i]
        b = string[i+1]
        a_ = string[i+2]
        if a == a_ and a != b:
            babs.append(b+a+b)

    return babs


def bab(string, babs):
    return any(bab_ in string for bab_ in babs)


with open("../inputs/07.txt") as f:
    ips = f.read().strip().split("\n")

tls = 0
ssl = 0
for ip in ips:
    strings = ip.replace("]", "[").split("[")
    inside = strings[0:len(strings):2]
    outside = strings[1:len(strings):2]

    if any(abba(s) for s in inside) and not any(abba(s) for s in outside):
        tls += 1

    babs = [bab_ for s in inside for bab_ in aba(s)]
    if babs and any(bab(s, babs) for s in outside):
        ssl += 1

print(f"Day 25 part 1: {tls}")
print(f"Day 25 part 2: {ssl}")
