data = sorted(open("../inputs/04.txt").read().strip().splitlines())
guards, gid, fh, fm, ah, am = {}, 0, 0, 0, 0, 0

for i in data:
    d = i.split()
    if "begins" in i:
        gid = int(d[3].strip('#'))
        if not guards.get(gid):
            guards[gid] = [0 for j in range(60)]
    if "falls" in i:
        fh, fm = map(int, d[1].strip(']').split(':'))
    if "wakes" in i:
        ah, am = map(int, d[1].strip(']').split(':'))
        for k in range((ah - fh) * 60 + (am - fm)):
            guards[gid][(fm + k) % 60] += 1

s = max([sum(guards[k]) for k in guards])
print("Day 4 part 1: " + str(next(k * guards[k].index(max(guards[k])) for k in guards for i in guards[k] if sum(guards[k]) == s)))

m = max([i for j in guards.values() for i in j])
print("Day 4 part 2: " + str(next(k * guards[k].index(i) for k in guards for i in guards[k] if i == m)))
