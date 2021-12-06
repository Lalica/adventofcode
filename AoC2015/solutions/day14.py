from itertools import cycle


seconds = 2503
reindeers, distance = [], []
with open("../inputs/14.txt") as f:
    for _, _, _, speed, _, _, fly, *_, rest, _ in map(str.split, f):
        speed, fly, rest = map(int, [speed, fly, rest])

        # total_time = fly + rest
        # whole_num = seconds // total_time * fly
        # reminder = min(fly, seconds % total_time)
        # distance.append((whole_num + reminder) * speed)

        reindeers.append(cycle([speed] * fly + [0] * rest))

n = len(reindeers)
score = [0] * n
distance = [0] * n
for _ in range(seconds):
    for reindeer, step in enumerate(reindeers):
        distance[reindeer] += next(step)

    best = max(distance)
    for reindeer in range(n):
        if distance[reindeer] == best:
            score[reindeer] += 1

print(f"Day 14 part 1: {max(distance)}")
print(f"Day 14 part 2: {max(score)}")
