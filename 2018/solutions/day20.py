dist = {0: 0}
move = {'N': 1j, 'S': -1j, 'W': -1, 'E': 1}


def walk(position, paths):
    for i in paths:
        if i in '|)$':
            return i == '|'
        elif i in 'NWSE':
            new_pos = position + move[i]
            if new_pos not in dist or dist[new_pos] > dist[position]:
                dist[new_pos] = dist[position] + 1
            position = new_pos
        elif i == '(':
            while walk(position, paths):
                pass
    return False


with open('../inputs/20.txt') as f:
    l = iter(next(f))
    next(l)
    walk(0, l)
    print('Day 20 part 1: ' + str(max(dist.values())))
    print('Day 20 part 2: ' + str(sum(r >= 1000 for r in dist.values())))

# code for part one without positions <3
# results = []
# def walk(steps, paths):
#     for i in paths:
#         if i in '|)$':
#             return steps, i != '|'
#         elif i in 'NWSE':
#             steps += 1
#         elif i == '(':
#             choices = []
#             while True:
#                 s, end = walk(steps, paths)
#                 choices.append(s)
#                 if end:
#                     if steps in choices:
#                         results.append(steps + (max(choices) - steps)/2)
#                     else:
#                         steps = max(choices)
#                     break
#     return steps, False
