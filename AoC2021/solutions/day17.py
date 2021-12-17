import re


with open("../inputs/17.txt") as f:
     x_min, x_max, y_min, y_max = map(int, re.findall(r"[-\d]+", f.read()))

highest_y = y_min + (abs(y_min) * (abs(y_min) + 1)) // 2
print(f"Day 17 part 1: {highest_y}")

velocities = 0
for v_x_init in range(min(0, x_min), max(0, x_max + 1)):
    for v_y_init in range(min(y_min, y_max), max(abs(y_min), abs(y_max)) + 1):
        x, y = 0, 0
        v_x, v_y = v_x_init, v_y_init
        while y > y_min:
            x += v_x
            y += v_y

            if v_x != 0:
                v_x -= 1 if v_x > 0 else -1
            v_y -= 1

            if x_min <= x <= x_max and y_min <= y <= y_max:
                velocities += 1
                break

print(f"Day 17 part 2: {velocities}")
