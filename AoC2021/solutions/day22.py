import re


def reboot(instructions):
    cubes = apply_instructions(instructions)
    return get_num_on(cubes)


def get_num_on(cubes):
    on = 0
    for c in cubes:
        on += (c[1] + 1 - c[0]) * (c[3] + 1 - c[2]) * (c[5] + 1 - c[4])
    return on

rotations = {
        0: lambda x, y, z: [x, y, z],
        1: lambda x, y, z: [x, -y, -z],
        2: lambda x, y, z: [x, z, -y],
        3: lambda x, y, z: [x, -z, y],
        4: lambda x, y, z: [-x, y, -z],
        5: lambda x, y, z: [-x, -y, z],
        6: lambda x, y, z: [-x, z, y],
        7: lambda x, y, z: [-x, -z, -y],
        8: lambda x, y, z: [y, x, -z],
        9: lambda x, y, z: [y, -x, z],
        10: lambda x, y, z: [y, z, x],
        11: lambda x, y, z: [y, -z, -x],
        12: lambda x, y, z: [-y, x, z],
        13: lambda x, y, z: [-y, -x, -z],
        14: lambda x, y, z: [-y, z, -x],
        15: lambda x, y, z: [-y, -z, x],
        16: lambda x, y, z: [z, x, y],
        17: lambda x, y, z: [z, -x, -y],
        18: lambda x, y, z: [z, y, -x],
        19: lambda x, y, z: [z, -y, x],
        20: lambda x, y, z: [-z, x, -y],
        21: lambda x, y, z: [-z, -x, y],
        22: lambda x, y, z: [-z, y, x],
        23: lambda x, y, z: [-z, -y, -x],
}
inv_rotations = {
    0: 0,
    1: 1,
    2: 3,
    3: 2,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 12,
    10: 16,
    11: 20,
    12: 9,
    13: 13,
    14: 21,
    15: 17,
    16: 10,
    17: 15,
    18: 22,
    19: 19,
    20: 11,
    21: 14,
    22: 18,
    23: 23,
}


def apply_instructions(instructions):
    cubes = []

    for switch, cube2 in instructions:
        new_cubes = []
        for cube1 in cubes:
            if is_crossing(cube1, cube2):
                a = split_cube(cube1, cube2)
                new_cubes += a
            else:
                new_cubes.append(cube1)
        cubes = new_cubes
        if switch:
            cubes.append(cube2)

    return cubes


def rotate(r, cube):
    xm, xM, ym, yM, zm, zM = cube
    cm = rotations[r](xm, ym, zm)
    cM = rotations[r](xM, yM, zM)

    for i in range(3):
        if cm[i] < cM[i]:
            cm[i], cM[i] = cM[i], cm[i]

    return [num for mM in zip(cm, cM) for num in mM]


def split_cube(cube1, cube2):
    for r in rotations:
        c1 = rotate(r, cube1)
        c2 = rotate(r, cube2)

        rule = get_rule(c1, c2)
        if rule == -1:
            continue

        new_cubes = split_types(c1, c2)[rule]
        return [rotate(inv_rotations[r], c) for c in new_cubes]


def is_crossing(cube1, cube2):
    x1m, x1M, y1m, y1M, z1m, z1M = cube1
    x2m, x2M, y2m, y2M, z2m, z2M = cube2

    return (
            x1M >= x2m and x2M >= x1m
            and y1M >= y2m and y2M >= y1m
            and z1M >= z2m and z2M >= z1m
    )


def get_rule(cube1, cube2):
    x1m, x1M, y1m, y1M, z1m, z1M = cube1
    x2m, x2M, y2m, y2M, z2m, z2M = cube2

    if (
        x1m < x2m and x1M > x2M
        and y1m < y2m and y1M > y2M
        and z1m < z2m and z1M > z2M
    ):
        return 0
    if (
        x1m < x2m and x1M > x2M
        and y1m < y2m and y1M > y2M
        and z1m >= z2m and z1M > z2M
    ):
        return 1
    if (
        x1m < x2m and x1M > x2M
        and y1m < y2m and y1M > y2M
        and z1m >= z2m and z1M <= z2M
    ):
        return 2
    if (
        x1m < x2m and x1M > x2M
        and y1m < y2m and y1M <= y2M
        and z1m >= z2m and z1M > z2M
    ):
        return 3
    if (
        x1m < x2m and x1M > x2M
        and y1m < y2m and y1M <= y2M
        and z1m >= z2m and z1M <= z2M
    ):
        return 4
    if (
        x1m >= x2m and x1M > x2M
        and y1m < y2m and y1M <= y2M
        and z1m >= z2m and z1M > z2M
    ):
        return 5
    if (
        x1m >= x2m and x1M > x2M
        and y1m < y2m and y1M <= y2M
        and z1m >= z2m and z1M <= z2M
    ):
        return 6
    if (
        x1m < x2m and x1M > x2M
        and y1m >= y2m and y1M <= y2M
        and z1m >= z2m and z1M <= z2M
    ):
        return 7
    if (
        x1m >= x2m and x1M > x2M
        and y1m >= y2m and y1M <= y2M
        and z1m >= z2m and z1M <= z2M
    ):
        return 8
    if (
        x1m >= x2m and x1M <= x2M
        and y1m >= y2m and y1M <= y2M
        and z1m >= z2m and z1M <= z2M
    ):
        return 9

    return -1


def split_types(cube1, cube2):
    s1, s2, s3, s4, s5, s6, s3m, s1m, s1mm = sections(cube1, cube2)
    t1 = [s1, s2, s3, s4, s5, s6]
    t2 = [s1, s2, s3, s4, s5]
    t3 = [s1, s2, s3, s4]
    t4 = [s1, s2, s3m, s4]
    t5 = [s1, s4, s2]
    t6 = [s1m, s1mm, s2]
    t7 = [s1m, s2]
    t8 = [s1, s2]
    t9 = [s2]
    t10 = []

    return [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]


def sections(cube1, cube2):
    x1m, x1M, y1m, y1M, z1m, z1M = cube1
    x2m, x2M, y2m, y2M, z2m, z2M = cube2

    s1 = [x1m, x2m-1, y1m, y1M, z1m, z1M]
    s2 = [x2M+1, x1M, y1m, y1M, z1m, z1M]
    s3 = [x2m, x2M, y2M+1, y1M, z1m, z1M]
    s4 = [x2m, x2M, y1m, y2m-1, z1m, z1M]
    s5 = [x2m, x2M, y2m, y2M, z2M+1, z1M]
    s6 = [x2m, x2M, y2m, y2M, z1m, z2m-1]
    s3m = [x2m, x2M, y2m, y1M, z2M+1, z1M]  # s5 if y1M == y2M
    s1m = [x1m, x2M, y1m, y2m-1, z1m, z1M]  # s4 if x1m == x2m
    s1mm = [x1m, x2M, y2m, y1M, z2M+1, z1M]  # s5 if y1m == y2m and x1m == x2m

    return [s1, s2, s3, s4, s5, s6, s3m, s1m, s1mm]


with open("../inputs/22.txt") as f:
    instructions = []
    for line in f:
        switch, ranges = line.split()
        instructions.append(
            [switch == "on", list(map(int, re.findall(r"[-\d]+", ranges)))]
        )

# generate inverse rotations
# cube = [-5, -2, 3, 7, -1, 21]
# for r in rotations:
#     for r2 in rotations:
#         if rotate(r2, rotate(r, cube)) == cube:
#             print(r, r2)

part1_instructions = [i for i in instructions if all(-50 <= n <= 50 for n in i[1])]
print(f"Day 22 part 1: {reboot(part1_instructions)}")
print(f"Day 22 part 2: {reboot(instructions)}")
