def eratosthenes_sieve(max_len, discs):
    nums = [0] * max_len
    for first, step in discs:
        i = first
        while i < len(nums):
            nums[i] += 1

            if nums[i] == len(discs):
                return i

            i += step

    return -1


def solve(discs):
    max_len = 1000000
    result = eratosthenes_sieve(max_len, discs)
    while result == -1:
        max_len *= 10
        result = eratosthenes_sieve(max_len, discs)

    return result


with open("../inputs/15.txt") as f:
    discs = []
    for i, line in enumerate(f):
        words = line.split()
        step = int(words[3])
        start = int(words[-1][:-1]) + i + 1
        first = (step - (start % step)) % step
        discs.append((first, step))

print(f"Day 15 part 1: {solve(discs)}")

discs.append((11 - (len(discs) + 1), 11))
print(f"Day 15 part 2: {solve(discs)}")
