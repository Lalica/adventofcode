with open("../inputs/20.txt") as f:
    num = int(next(f))

end = num // 20
nums1, nums2 = [0] * end, [0] * end
part1, part2 = 0, 0
for i in range(1, end):
    current = i

    if not part1 and nums1[i] + current * 10 >= num:
        part1 = i

    if not part2 and nums2[i] + current * 11 >= num:
        part2 = i

    if part1 and part2:
        print(f"Day 20 part 1: {part1}")
        print(f"Day 20 part 2: {part2}")
        exit()

    cnt = 1
    while current < end:
        nums1[current] += i * 10

        if cnt < 50:
            nums2[current] += i * 11
            cnt += 1

        current += i
