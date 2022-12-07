from computer import read_file, opcode


with open('../inputs/05.txt') as f:
    data = read_file(f)

print('Provide 1')
opcode(data[:])
print(f'Day 5 part 1 is one LINE ABOVE')

print('\nProvide 5')
opcode(data[:])
print(f'Day 5 part 2 is one LINE ABOVE')
