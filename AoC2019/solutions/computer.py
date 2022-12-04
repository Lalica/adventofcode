def opcode(data):
    i = 0
    while i < len(data):
        code, a, b, c = data[i:i+4]

        if code == 99:
            return data[0]
        elif code == 1:
            data[c] = data[a] + data[b]
        elif code == 2:
            data[c] = data[a] * data[b]
        else: 
            break

        i += 4

    return -1
