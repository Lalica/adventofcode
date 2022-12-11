from math import prod
from collections import deque


def monkey_business(monkeys, rounds, worry):
    inspections = [0] * len(monkeys)
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            while monkey["items"]:
                item = monkey["items"].popleft()
                item = monkey["operation"](item)
                item = worry(item)
                to_throw = item % monkey["test"] == 0
                j = monkey[to_throw]
                monkeys[j]["items"].append(item)

                inspections[i] += 1

    return inspections


monkeys = []
starting_items = []
with open("../inputs/11.txt") as f:
    for chunk in f.read().split("\n\n"):
        monkey = {}
        for line in chunk.splitlines():
            key, value = line.strip().split(":")
            match key:
                case "Starting items":
                    items = deque(map(int, value.split(", ")))
                    monkey["items"] = items.copy()
                    starting_items.append(items)
                case "Operation":
                    monkey["operation"] = eval("lambda " + value.replace("new =", "old:"))
                case "Test":
                    monkey["test"] = int(value.split()[-1])
                case "If true":
                    monkey[True] = int(value.split()[-1])
                case "If false":
                    monkey[False] = int(value.split()[-1])

        monkeys.append(monkey)


inspections = monkey_business(monkeys, 20, lambda x: x // 3)
part1 = prod(sorted(inspections)[-2:])
print(f'Day 11 part 1: {part1}')

for i in range(len(monkeys)):
    monkeys[i]["items"] = starting_items[i]

mod = prod(monkey["test"] for monkey in monkeys)
inspections = monkey_business(monkeys, 10000, lambda x: x % mod)
part2 = prod(sorted(inspections)[-2:])
print(f'Day 11 part 2: {part2}')
