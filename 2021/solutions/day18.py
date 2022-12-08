from copy import deepcopy


def add_num(num, n, i):
    if isinstance(num, list) and isinstance(num[i], int):
        num[i] += n
    else:
        add_num(num[i], n, i)


def expload(num, depth=1):
    if isinstance(num, int):
        return -1, -1, False

    if depth > 4:
        if isinstance(num, list) and isinstance(num[0], int) and isinstance(num[1], int):
            return *num, False

    for i in [0, 1]:
        left, right, exploaded = expload(num[i], depth + 1)

        this_side, other_side = [right, left] if i else [left, right]
        return_lr = [[left, -1], [-1, right]]

        if exploaded:
            return left, right, exploaded
        if left != -1 and right != -1:
            num[i] = 0
        if other_side != -1:
            if isinstance(num[not i], int):
                num[not i] += other_side
            else:
                add_num(num[not i], other_side, i)
            return *return_lr[i], this_side == -1
        if this_side != -1:
            return *return_lr[i], False

    return -1, -1, False


def split(num):
    if isinstance(num, int):
        return False

    for index in [0, 1]:
        if isinstance(num[index], int) and num[index] >= 10:
            div, mod = divmod(num[index], 2)
            num[index] = [div, div + mod]
            return True

        if split(num[index]):
            return True

    return False


def magnitude(num):
    if isinstance(num, int):
        return num
    return 3 * magnitude(num[0]) + 2 * magnitude(num[1])


def add_and_reduce(num1, num2):
    sum_ = [deepcopy(num1), deepcopy(num2)]
    while True:
        left, right, exploaded = expload(sum_)
        if exploaded or left != -1 or right != -1:
            continue
        if not split(sum_):
            break
    return sum_


with open("../inputs/18.txt") as f:
    numbers = [eval(line) for line in f]

sum_ = numbers[0]
for num in numbers[1:]:
    sum_ = add_and_reduce(sum_, num)
print(f"Day 18 part 1: {magnitude(sum_)}")

max_ = 0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            max_ = max(max_, magnitude(add_and_reduce(numbers[i], numbers[j])))
print(f"Day 18 part 2: {max_}")
