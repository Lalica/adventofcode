from re import findall


data = sorted(open("../inputs/04.txt").read().strip().splitlines())
guards, gid, fh, fm, ah, am = {}, 0, 0, 0, 0, 0

for i in data:
    d = map(int, findall(r'\d+', i))
    if "begins" in i:
        gid = d[-1]
        if not guards.get(gid):
            guards[gid] = [0 for j in range(60)]
    elif "falls" in i:
        fh, fm = d[3], d[4]
    else:
        ah, am = d[3], d[4]
        for k in range((ah - fh) * 60 + (am - fm)):
            guards[gid][(fm + k) % 60] += 1

s = max([sum(guards[k]) for k in guards])
print("Day 4 part 1: " + str(next(k * guards[k].index(max(guards[k])) for k in guards for i in guards[k] if sum(guards[k]) == s)))

m = max([i for j in guards.values() for i in j])
print("Day 4 part 2: " + str(next(k * guards[k].index(i) for k in guards for i in guards[k] if i == m)))
