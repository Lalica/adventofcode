from collections import defaultdict


def map_beacons(distances1, distances2):
    beacon_dist1 = defaultdict(set)
    beacon_dist2 = defaultdict(set)

    for beacon_dist, distances in [[beacon_dist1, distances1], [beacon_dist2, distances2]]:
        for beacon1, beacon2, distance in distances:
            beacon_dist[beacon1].add(distance)
            beacon_dist[beacon2].add(distance)

    beacon_pairs = []
    for beacon1 in beacon_dist1:
        for beacon2 in beacon_dist2:
            if beacon_dist1[beacon1] == beacon_dist2[beacon2]:
                beacon_pairs.append([beacon1, beacon2])

    return beacon_pairs


def same_distance_pairs(i, j):
    same_distances = [
            d1
            for _, _, d1 in distances[i]
            if d1 in [d2 for _, _, d2 in distances[j]]
    ]
    distances_i = [d for d in distances[i] if d[2] in same_distances]
    distances_j = [d for d in distances[j] if d[2] in same_distances]

    return distances_i, distances_j


def get_rotation(i, j, beacon_to_beacon):
    for r in rotations:
        ib, jb = beacon_to_beacon[0]
        b1, b2 = scanners[i][ib], rotations[r](*scanners[j][jb])
        sh = [b1[i] - b2[i] for i in range(3)]

        for ib, jb in beacon_to_beacon:
            b1, b2 = scanners[i][ib], scanners[j][jb]
            b2 = shift(rotations[r](*b2), sh)
            if b1 != b2:
                break
        else:
            return r, sh


def shift(beacon, sh):
    return [beacon[i] + sh[i] for i in range(3)]


def eucilidian(t1, t2):
    x1, y1, z1 = t1
    x2, y2, z2 = t2
    return pow(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2), 0.5)


def manhattan(t1, t2):
    x1, y1, z1 = t1
    x2, y2, z2 = t2
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


with open("../inputs/19.txt") as f:
    scanners = [
            [
                list(map(int, line.split(",")))
                for line in scanner.split("\n")[1:]
            ]
            for scanner in f.read().strip().split("\n\n")
    ]

rotations = {
        0: lambda x, y, z: [x, y, z],
        1: lambda x, y, z: [x, -y, -z],
        2: lambda x, y, z: [x, z, -y],
        3: lambda x, y, z: [x, -z, y],
        4: lambda x, y, z: [-x, y, -z],
        5: lambda x, y, z: [-x, -y, z],
        6: lambda x, y, z: [-x, z, y],
        7: lambda x, y, z: [-x, -z, -y],
        8: lambda x, y, z: [y, x, -z],
        9: lambda x, y, z: [y, -x, z],
        10: lambda x, y, z: [y, z, x],
        11: lambda x, y, z: [y, -z, -x],
        12: lambda x, y, z: [-y, x, z],
        13: lambda x, y, z: [-y, -x, -z],
        14: lambda x, y, z: [-y, z, -x],
        15: lambda x, y, z: [-y, -z, x],
        16: lambda x, y, z: [z, x, y],
        17: lambda x, y, z: [z, -x, -y],
        18: lambda x, y, z: [z, y, -x],
        19: lambda x, y, z: [z, -y, x],
        20: lambda x, y, z: [-z, x, -y],
        21: lambda x, y, z: [-z, -x, y],
        22: lambda x, y, z: [-z, y, x],
        23: lambda x, y, z: [-z, -y, -x],
}

distances = [
        [
            [i, j, eucilidian(scanner[i], scanner[j])]
            for i in range(len(scanner)) for j in range(i + 1, len(scanner))
        ]
        for scanner in scanners
]

to_connect = [
        (i, j)
        for i in range(len(distances))
        for j in range(i + 1, len(distances))
        if sum([d1 in [d2 for _, _, d2 in distances[j]] for _, _, d1 in distances[i]]) >= 66
]

trench_map = {tuple(beacon) for beacon in scanners[0]}
added = {0}
rotation_for_scanner = {0: []}
trench_scanners = [[0, 0, 0]]

while len(added) < len(scanners):
    for i in list(added):
        for j in [s[1] if s[0] == i else s[0] for s in to_connect if i in s]:
            if j in added:
                continue

            r, sh = get_rotation(i, j, map_beacons(*same_distance_pairs(i, j)))
            rotation_for_scanner[j] = [[r, sh]] + rotation_for_scanner[i]

            for beacon in scanners[j]:
                trans_beacon = beacon
                for r, sh in rotation_for_scanner[j]:
                    trans_beacon = shift(rotations[r](*trans_beacon), sh)
                trench_map.add(tuple(trans_beacon))

            trans_scanner = [0, 0, 0]
            for r, sh in rotation_for_scanner[j]:
                trans_scanner = shift(rotations[r](*trans_scanner), sh)
            trench_scanners.append(trans_scanner)

            added.add(j)

print(f"Day 19 part 1: {len(trench_map)}")

max_scanner_distance = max(manhattan(t1, t2) for t1 in trench_scanners for t2 in trench_scanners)
print(f"Day 19 part 2: {max_scanner_distance}")
