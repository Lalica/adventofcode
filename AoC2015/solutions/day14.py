import math
from itertools import cycle


reindeers, distance = [], []
seconds = 2503
with open("../inputs/14.txt") as f:
    for _, _, _, speed, _, _, run, *_, rest, _ in map(str.split, f):
        speed, run, rest = int(speed), int(run), int(rest)
        time = run + rest
        floor = math.floor(seconds / time)
        reminder = min(run, seconds - floor * time)
        distance.append((floor * run + reminder) * speed)

        reindeers.append(cycle([speed] * run + [0] * rest))

print(f"Day 14 part 1: {max(distance)}")

n = len(reindeers)
score = [0] * n
km_s = [0] * n
for _ in range(seconds):
    for reindeer, step in enumerate(reindeers):
        km_s[reindeer] += next(step)

    best = max(km_s)
    for reindeer in range(n):
        if km_s[reindeer] == best:
            score[reindeer] += 1

print(f"Day 14 part 2: {max(score)}")
