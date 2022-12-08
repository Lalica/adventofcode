with open("../inputs/08.txt") as f:
    displays = [line.split(" | ") for line in f]

len_to_num = {2: [1], 3: [7], 4: [4], 7: [8], 5: [2, 3, 5], 6: [0, 6, 9]}
unique = [length for length in len_to_num if len(len_to_num[length]) == 1]

sum_ = 0
for _, code in displays:
    sum_ += sum(len(num) in unique for num in code.split())

print(f"Day 8 part 1: {sum_}")

sum_ = 0
for segments, code in displays:
    nums = [[] for _ in range(10)]

    for segment in segments.split():
        for num in len_to_num[len(segment)]:
            nums[num].append(set(segment))

    nums[1] = nums[1][0]
    nums[4] = nums[4][0]
    nums[7] = nums[7][0]
    nums[8] = nums[8][0]
    nums[3] = [seg for seg in nums[3] if nums[1].issubset(seg)][0]
    nums[9] = [seg for seg in nums[9] if nums[4].issubset(seg)][0]
    nums[5] = [seg for seg in nums[5] if seg.issubset(nums[9]) and seg != nums[3]][0]
    nums[2] = [seg for seg in nums[2] if seg not in [nums[5], nums[3]]][0]
    nums[6] = [seg for seg in nums[6] if nums[5].issubset(seg) and not nums[4].issubset(seg)][0]
    nums[0] = [seg for seg in nums[0] if seg not in [nums[6], nums[9]]][0]

    code_nums = [str(nums.index(set(c))) for c in code.split()]
    sum_ += int("".join(code_nums))

print(f"Day 8 part 2: {sum_}")
