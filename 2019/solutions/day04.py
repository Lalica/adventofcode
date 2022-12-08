with open('../inputs/04.txt') as f:
    start, end = map(int, f.read().split('-'))

part1, part2 = 0, 0
for num in range(start, end + 1):
    num = str(num)
    occurances = 1
    repeated1, repeated2 = False, False
    for i in range(len(num) - 1):
        if num[i + 1] < num[i]:
            break

        if num[i + 1] == num[i]:
            occurances += 1
            repeated1 = True
        else:
            if occurances == 2:
                repeated2 = True
            occurances = 1
    else:
        if repeated1 or occurances > 1:
            part1 += 1
        if repeated2 or occurances == 2:
            part2 += 1

print(f'Day 2 part 1: {part1}')
print(f'Day 2 part 2: {part2}')
