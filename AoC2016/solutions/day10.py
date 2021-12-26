from collections import defaultdict


instructions = dict()
bots = defaultdict(list)
outputs = defaultdict(list)
with open("../inputs/10.txt") as f:
    for line in f:
        line = line.split()
        if line[0] == "value":
            bot = int(line[5])
            microchip = int(line[1])
            bots[bot].append(microchip)
        else:
            bot = int(line[1])
            low = int(line[6])
            is_low_output = line[5] == "output"
            high = int(line[-1])
            is_high_output = line[-2] == "output"
            instructions[bot] = [(is_low_output, low), (is_high_output, high)]

bot_q = [k for k, v in bots.items() if len(v) == 2]
while len(bot_q):
    bot = bot_q.pop(0)
    low, high = sorted(bots[bot])
    bots[bot] = []

    if low == 17 and high == 61:
        print(f"Day 10 part 1: {bot}")

    low_, high_ = instructions[bot]
    is_low_output, low_out = low_
    is_high_output, high_out = high_

    if is_low_output:
        outputs[low_out].append(low)
    else:
        bots[low_out].append(low)
        if len(bots[low_out]) == 2:
            bot_q.append(low_out)

    if is_high_output:
        outputs[high_out].append(high)
    else:
        bots[high_out].append(high)
        if len(bots[high_out]) == 2:
            bot_q.append(high_out)

mul = outputs[0][0] * outputs[1][0] * outputs[2][0]
print(f"Day 10 part 2: {mul}")
