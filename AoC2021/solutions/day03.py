from collections import Counter


def shrink(nums, take_most_common, if_equal):
    index = 0 if take_most_common else 1

    if len(nums) > 1:
        digits = [num[i] for num in nums]
        cnt = Counter(digits).most_common()
        chosen_num = if_equal if cnt[0][1] == cnt[1][1] else cnt[index][0]
        nums = [num for num in nums if num[i] == chosen_num]

    return nums


with open("../inputs/03.txt") as f:
    numbers = list(line.strip() for line in f)

gamma, epsilon = "", ""
nums_og = numbers.copy()
nums_cs = numbers.copy()

for i in range(len(numbers[0])):
    digits = [num[i] for num in numbers]
    cnt = Counter(digits).most_common()
    gamma += cnt[0][0]
    epsilon += cnt[1][0]

    nums_og = shrink(nums_og, take_most_common=True,  if_equal="1")
    nums_cs = shrink(nums_cs, take_most_common=False, if_equal="0")

part1 = int(gamma, 2) * int(epsilon, 2)
print(f'Day 3 part 1: {part1}')

part2 = int(nums_og[0], 2) * int(nums_cs[0], 2)
print(f'Day 3 part 2: {part2}')
