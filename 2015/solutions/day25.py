with open("../inputs/25.txt") as f:
    *_, row, _, col = f.read().split()
    row, col = int(row[:-1]), int(col[:-1])

rc = row + col
n = (rc ** 2 - rc) // 2 - row

code, mul, div = 20151125, 252533, 33554393
code = code * pow(mul, n, div) % div

print(f"Day 25: {code}")
