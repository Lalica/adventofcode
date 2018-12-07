from collections import defaultdict


data = [(i[1], i[7]) for i in map(str.split, open("../inputs/07.txt").read().strip().splitlines())]
l1, l2, d = set(i[0] for i in data), set(i[1] for i in data), defaultdict(list)
p1, p2, d2 = set(l1), set(l2), defaultdict(list)
workers, queue, a, count = [1, 1, 1, 1, 1], ['', '', '', '', ''], 60 - 64,  -1

for i in data:
    d[i[1]].append(i[0])
    d2[i[1]].append(i[0])

l3, s = l1.difference(l2), ""
p3, s2 = set(l3), ""

while len(l3):
    first = sorted(l3)[0]
    s += first
    l1.remove(first)
    for k in d:
        if first in d[k]:
            d[k].remove(first)
        if len(d[k]) == 0 and k in l2:
            l1.add(k)
            l2.remove(k)
    l3 = l1.difference(l2)

print("Day 7 part 1: " + s)

while len(p3):
    workers = [max(i - 1, 0) for i in workers]

    for q in range(5):
        if workers[q] != 0 or queue[q] == '':
            continue
        if queue[q] in p1:
            p1.remove(queue[q])
            s2 += queue[q]
        for k in d2:
            if queue[q] in d2[k]:
                d2[k].remove(queue[q])
            if len(d2[k]) == 0 and k in p2:
                p1.add(k)
                p2.remove(k)
        queue[q] = ''
    p3 = p1.difference(p2)
    first = sorted(p3.difference(queue))[:workers.count(0)]
    for f in first:
        queue[workers.index(0)] = f
        workers[workers.index(0)] = ord(f) + a

    count += 1

print("Day 7 part 2: " + s2 + " " + str(count))
