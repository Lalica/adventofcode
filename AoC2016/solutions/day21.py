def scramble(word, reverse=False):
    for line in instructions:
        cmd, obj, x, *_, y = line.split()

        if cmd == "swap":
            if obj == "position":
                i, j = int(x), int(y)
            elif obj == "letter":
                i, j = [i for i, c in enumerate(word) if c in {x, y}]

            word[i], word[j] = word[j], word[i]
        elif cmd == "reverse":
            x, y = int(x), int(y)
            word = word[:x] + list(reversed(word[x: y + 1])) + word[y + 1:]
        elif cmd == "rotate":
            if obj == "left":
                num = int(x)
            elif obj == "right":
                num = -int(x)
            elif obj == "based":
                x = next(i for i, c in enumerate(word) if c == y)
                num = x + 1 + (x >= 4)
                if reverse:
                    num = {1: 1, 3: 2, 5: 3, 7: 4, 2: 6, 4: 7, 6: 8, 0: 1}[x]
                num *= -1
            if reverse:
                num *= -1
            word = word[num:] + word[:num]
        elif cmd == "move":
            i, j = int(x), int(y)
            if reverse:
                i, j = j, i
            c = word[i]
            del word[i]
            word.insert(j, c)

    return "".join(word)


with open("../inputs/21.txt") as f:
    instructions = list(f)

result = scramble(list("abcdefgh"))
print(f"Day 20 part 1: {result}")

instructions.reverse()
result = scramble(list("fbgdceah"), True)
print(f"Day 20 part 2: {result}")
