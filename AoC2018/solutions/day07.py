from collections import defaultdict


def graph(d, m1, m2, m3, workers, queue, offset, wn):
    count, s = -1, ""
    while len(m3):
        workers = [max(i - 1, 0) for i in workers]
        for i in range(wn):
            if workers[i] != 0 or queue[i] == '':
                continue
            if queue[i] in m1:
                m1.remove(queue[i])
                s += queue[i]
            for k in d:
                if queue[i] in d[k]:
                    d[k].remove(queue[i])
                if len(d[k]) == 0 and k in m2:
                    m1.add(k)
                    m2.remove(k)
            queue[i] = ''
        m3 = m1.difference(m2)
        first = sorted(m3.difference(queue))[:workers.count(0)]
        for f in first:
            queue[workers.index(0)] = f
            workers[workers.index(0)] = ord(f) + offset

        count += 1

    return count, s


data = [(i[1], i[7]) for i in map(str.split, open("../inputs/07.txt").read().strip().splitlines())]
l1, l2, d1 = set(i[0] for i in data), set(i[1] for i in data), defaultdict(list)
p1, p2, d2, w, q, o = set(l1), set(l2), defaultdict(list), [1, 1, 1, 1, 1], ['', '', '', '', ''], 60 - 64

for i in data:
    d1[i[1]].append(i[0])
    d2[i[1]].append(i[0])

l3 = l1.difference(l2)
p3 = set(l3)

print("Day 7 part 1: " + graph(d1, l1, l2, l3, [1], [''], -100, 1)[1])
print("Day 7 part 2: " + str(graph(d2, p1, p2, p3, w, q, o, 5)[0]))
