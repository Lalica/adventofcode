import re


def reboot(instructions):
    cubes = apply_instructions(instructions)
    on = sum((c[1] + 1 - c[0]) * (c[3] + 1 - c[2]) * (c[5] + 1 - c[4]) for c in cubes)
    return on


def apply_instructions(instructions):
    cubes = []
    for switch, cube2 in instructions:
        new_cubes = []
        for cube1 in cubes:
            if is_crossing(cube1, cube2):
                new_cubes += get_difference(cube1, cube2)
            else:
                new_cubes.append(cube1)

        cubes = new_cubes
        if switch:
            cubes.append(cube2)

    return cubes


def is_crossing(cube1, cube2):
    x1m, x1M, y1m, y1M, z1m, z1M = cube1
    x2m, x2M, y2m, y2M, z2m, z2M = cube2

    return (
            x1M >= x2m and x2M >= x1m
            and y1M >= y2m and y2M >= y1m
            and z1M >= z2m and z2M >= z1m
    )


def get_difference(cube1, cube2):
    for r in rotations:
        c1 = rotate(r, cube1)
        c2 = rotate(r, cube2)

        new_cubes = split_cube(c1, c2)
        if new_cubes is None:
            continue

        return [rotate(inv_rotations[r], c) for c in new_cubes]


def rotate(r, cube):
    xm, xM, ym, yM, zm, zM = cube
    cm = rotations[r](xm, ym, zm)
    cM = rotations[r](xM, yM, zM)

    for i in range(3):
        if cm[i] > cM[i]:
            cm[i], cM[i] = cM[i], cm[i]

    return [num for mM in zip(cm, cM) for num in mM]


def split_cube(cube1, cube2):
    x1m, x1M, y1m, y1M, z1m, z1M = cube1
    x2m, x2M, y2m, y2M, z2m, z2M = cube2

    s1 = [x2M+1, x1M, y1m, y1M, z1m, z1M]
    s2 = [x1m, x2m-1, y1m, y1M, z1m, z1M]
    s3 = [x2m, x2M, y2M+1, y1M, z1m, z1M]
    s4 = [x2m, x2M, y1m, y2m-1, z1m, z1M]
    s2m = [x1m, x2M, y1m, y2m-1, z1m, z1M]  # s4 if x1m == x2m
    s5 = [x2m, x2M, y2m, y2M, z2M+1, z1M]
    s3m = [x2m, x2M, y2m, y1M, z2M+1, z1M]  # s5 if y1M == y2M
    s2mm = [x1m, x2M, y2m, y1M, z2M+1, z1M]  # s5 if y1m == y2m and x1m == x2m
    s6 = [x2m, x2M, y2m, y2M, z1m, z2m-1]

    if (
        x1m < x2m and x1M > x2M
        and y1m < y2m and y1M > y2M
        and z1m < z2m and z1M > z2M
    ):
        return [s1, s2, s3, s4, s5, s6]
    if (
        x1m < x2m and x1M > x2M
        and y1m < y2m and y1M > y2M
        and z1m >= z2m and z1M > z2M
    ):
        return [s1, s2, s3, s4, s5]
    if (
        x1m < x2m and x1M > x2M
        and y1m < y2m and y1M > y2M
        and z1m >= z2m and z1M <= z2M
    ):
        return [s1, s2, s3, s4]
    if (
        x1m < x2m and x1M > x2M
        and y1m < y2m and y1M <= y2M
        and z1m >= z2m and z1M > z2M
    ):
        return [s1, s2, s3m, s4]
    if (
        x1m < x2m and x1M > x2M
        and y1m < y2m and y1M <= y2M
        and z1m >= z2m and z1M <= z2M
    ):
        return [s1, s2, s4]
    if (
        x1m >= x2m and x1M > x2M
        and y1m < y2m and y1M <= y2M
        and z1m >= z2m and z1M > z2M
    ):
        return [s1, s2m, s2mm]
    if (
        x1m >= x2m and x1M > x2M
        and y1m < y2m and y1M <= y2M
        and z1m >= z2m and z1M <= z2M
    ):
        return [s1, s2m]
    if (
        x1m < x2m and x1M > x2M
        and y1m >= y2m and y1M <= y2M
        and z1m >= z2m and z1M <= z2M
    ):
        return [s1, s2]
    if (
        x1m >= x2m and x1M > x2M
        and y1m >= y2m and y1M <= y2M
        and z1m >= z2m and z1M <= z2M
    ):
        return [s1]
    if (
        x1m >= x2m and x1M <= x2M
        and y1m >= y2m and y1M <= y2M
        and z1m >= z2m and z1M <= z2M
    ):
        return []

    return None


def get_inverse_rotations():
    sample_cube = [2, 3, 5, 7, 11, 13]

    inv = dict()
    for r1 in rotations:
        for r2 in rotations:
            if rotate(r2, rotate(r1, sample_cube)) == sample_cube:
                inv[r1] = r2
                break

    return inv


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
inv_rotations = get_inverse_rotations()

with open("../inputs/22.txt") as f:
    steps = []
    for line in f:
        switch, cube = line.split()
        steps.append([switch == "on", list(map(int, re.findall(r"[-\d]+", cube)))])

initialization = [i for i in steps if all(-50 <= n <= 50 for n in i[1])]
print(f"Day 22 part 1: {reboot(initialization)}")
print(f"Day 22 part 2: {reboot(steps)}")
