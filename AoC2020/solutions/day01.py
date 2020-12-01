with open('../inputs/01.txt') as f:
    nums = [int(line) for line in f]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == 2020:
            part1 = nums[i] * nums[j]
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 2020:
                part2 = nums[i] * nums[j] * nums[k]

print(f'Day 1 part 1: {part1}')
print(f'Day 1 part 2: {part2}')
