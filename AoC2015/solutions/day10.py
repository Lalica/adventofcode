def look_and_say(count, input):
    for j in range(count):
        num, temp = 1, []

        for i in range(1, len(input)):
            if input[i] == input[i - 1]:
                num += 1
            else:
                temp.append(num)
                temp.append(input[i - 1])
                num = 1

        temp.append(num)
        temp.append(len(input) - 1)
        input = temp
    return input


with open('../inputs/10.txt') as f:
    input = [int(i) for i in list(f.read().strip())]

input = look_and_say(40, input)
print("Day 10 part 1: " + str(len(input)))
input = look_and_say(10, input)
print("Day 10 part 2: " + str(len(input)))
