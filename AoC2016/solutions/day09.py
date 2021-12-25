def decompress(file, version=1):
    len_ = 0
    prev_i = 0
    while prev_i < len(file):
        i = file.find("(", prev_i)
        if i == -1:
            len_ += len(file) - prev_i
            break
        j = file.find(")", i)
        x, y = map(int, file[i+1:j].split("x"))

        len_ += i - prev_i
        prev_i = j + 1 + x

        if version == 1:
            inner_len = x
        else:
            inner_len = decompress(file[j+1:j+1+x], version)
        len_ += inner_len * y

    return len_


with open("../inputs/09.txt") as f:
    file = f.read().strip()

print(f"Day 9 part 1: {decompress(file, version=1)}")
print(f"Day 9 part 2: {decompress(file, version=2)}")
