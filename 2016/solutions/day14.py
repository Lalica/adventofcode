from hashlib import md5
from itertools import groupby


def get_groups(s):
    groups = groupby(s)
    groups = [(key, sum(1 for _ in group)) for key, group in groups]
    five = [key for key, cnt in groups if cnt >= 5]
    triplet = next((key for key, cnt in groups if cnt >= 3), None)
    return triplet, five


def get_md5(s, stretch):
    md5_hash = md5(s.encode()).hexdigest()

    for i in range(1, stretch + 1):
        md5_hash = md5(md5_hash.encode()).hexdigest()

    return md5_hash


def get_keys(stretch=0):
    triplets = []
    keys = set()

    i = 0
    end = None
    while not end or i <= end:
        md5_hash = get_md5(salt + str(i), stretch)
        triplet, five_seq = get_groups(md5_hash)
        triplets.append(triplet)

        for j in range(max(0, i - 1000), i):
            if triplets[j] in five_seq:
                keys.add(j)
                if len(keys) == 64:
                    end = j + 1000

        i += 1

    return sorted(keys)[63]


with open("../inputs/14.txt") as f:
    salt = f.read().strip()

print(f"Day 14 part 1: {get_keys()}")
print(f"Day 14 part 2: {get_keys(stretch=2016)}")
