with open('../inputs/14.txt') as f:
    data = [line.strip() for line in f]

memory1 = dict()
memory2 = dict()


def writeRec(i, mask, value):
    if i == 36:
        memory2[int(''.join(mask), 2)] = value
        return

    if mask[i] == 'X':
        mask[i] = '0'
        writeRec(i+1, mask.copy(), value)
        mask[i] = '1'
        writeRec(i+1, mask.copy(), value)
    else:
        writeRec(i+1, mask, value)


for d in data:
    if d.startswith('mask'):
        mask = d[7:]
        maskOr = int(mask.replace('X', '0'), 2)
        maskAnd = int(mask.replace('X', '1'), 2)
    if d.startswith('mem'):
        address, num = map(int, d[4:].split('] = '))
        memory1[address] = (num | maskOr) & maskAnd

        ad = list(format(address | maskOr, '036b'))
        ad = ['X' if mask[i] == 'X' else ad[i] for i in range(len(mask))]
        writeRec(0, ad, num)


part1 = sum(memory1.values())
part2 = sum(memory2.values())
print(f'Day 14 part 1: {part1}')
print(f'Day 14 part 2: {part2}')
