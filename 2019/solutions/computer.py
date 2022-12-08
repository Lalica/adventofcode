nums_params = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        99: 0
}

MAX_PARAMS = 3

mode_override = {
        1: (2, 1),
        2: (2, 1),
        3: (0, 1),
        7: (2, 1),
        8: (2, 1),
}


def read_file(f):
    return list(map(int, f.read().strip().split(',')))


def opcode(data):
    i = 0
    while i < len(data):
        code, modes = get_code_and_modes(data[i])
        if code not in nums_params:
            break

        num_params = nums_params[code]
        a, b, c = get_params(data, i, num_params, modes)

        if code == 99:
            return data[0]
        elif code == 1:
            data[c] = a + b
        elif code == 2:
            data[c] = a * b
        elif code == 3:
            num = int(input("Insert number: "))
            data[a] = num
        elif code == 4:
            print(a)
        elif code == 5:
            if a != 0:
                i = b - num_params - 1
        elif code == 6:
            if a == 0:
                i = b - num_params - 1
        elif code == 7:
            data[c] = int(a < b)
        elif code == 8:
            data[c] = int(a == b)

        i += num_params + 1

    return float("inf")


def get_params(data, i, num_params, modes):
    params = data[i + 1:i + 1 + num_params]
    params += [0] * (MAX_PARAMS - num_params)
    
    return [get_value(data, params[i], modes[i]) for i in range(MAX_PARAMS)]


def get_code_and_modes(num):
    code = num % 100

    explicit_modes = str(num // 100)
    implicit_modes = "0" * (MAX_PARAMS - len(explicit_modes))
    modes = list(map(int, implicit_modes + explicit_modes))[::-1]
    if code in mode_override:
        i, val = mode_override[code]
        modes[i] = val

    return code, modes


def get_value(data, param, mode):
    return param if mode else data[param]
