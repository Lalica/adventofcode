from collections import deque


with open('../inputs/09.txt') as f:
    numbers = [int(line) for line in f]

window, invalid = 25, -1
for i in range(len(numbers)-window):
    current = numbers[window+i]
    preamble = numbers[i:window+i]
    found = False
    for p in preamble:
        if (current - p) in preamble:
            found = True
            break
    if not found:
        invalid = current
        break

cont_range, cont_sum = deque(), 0
part2 = 0
for n in numbers:
    cont_range.append(n)
    cont_sum += n

    while cont_sum > invalid:
        cont_sum -= cont_range.popleft()

    if cont_sum == invalid and len(cont_range) > 1:
        part2 = min(cont_range) + max(cont_range)
        break

# brute force
# for i in range(2, len(numbers)//2):
#     for j in range(0, len(numbers)-i):
#         if sum(numbers[j:j+i]) == invalid:
#             part2 = min(numbers[j:j+i]) + max(numbers[j:j+i])
#             break
#     else:
#         continue
#     break

print(f'Day 9 part 1: {invalid}')
print(f'Day 9 part 2: {part2}')
