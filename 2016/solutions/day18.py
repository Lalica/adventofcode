with open("../inputs/18.txt") as f:
    first_row = [c == "." for c in f.read().strip()]

for n in [40, 400000]:
    row_len = len(first_row)
    safe = sum(first_row)
    row = [True] + first_row + [True]
    for i in range(n - 1):
        row = [not (row[i] ^ row[i + 2]) for i in range(len(row) - 2)]
        safe += sum(row)
        row = [True] + row + [True]

    print(f"Day 18 part {int(n != 40) + 1}: {safe}")
