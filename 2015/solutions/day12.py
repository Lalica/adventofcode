import json


def recurse(data, exclude=None):
    if isinstance(data, int):
        return data

    sum_ = 0
    if isinstance(data, dict):
        if exclude in data.values():
            return 0
        sum_ += sum(recurse(value, exclude) for value in data.values())

    if isinstance(data, list):
        sum_ += sum(recurse(value, exclude) for value in data)

    return sum_


with open("../inputs/12.txt") as f:
    data = json.load(f)

part1 = recurse(data)
print(f"Day 12 part 1: {part1}")
part2 = recurse(data, exclude="red")
print(f"Day 12 part 2: {part2}")
