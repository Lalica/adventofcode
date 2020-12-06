from collections import Counter


with open('../inputs/06.txt') as f:
    data = f.read().strip().split('\n\n')

cnt1 = 0
cnt2 = 0
for group in data:
    votes = group.split('\n')
    counter = Counter()
    for vote in votes:
        counter.update(vote)
    cnt1 += len(counter)
    cnt2 += sum(v[1] == len(votes) for v in counter.items())

print(f'Day 6 part 1: {cnt1}')
print(f'Day 6 part 2: {cnt2}')
