from collections import defaultdict


with open("../inputs/17.txt") as f:
    initial_data = [list(line) for line in f]
n, m = len(initial_data), len(initial_data[0])
state1 = set((i, j, 0) for j in range(n) for i in range(m) if initial_data[j][i] == '#')
state2 = set((i, j, 0, 0) for j in range(n) for i in range(m) if initial_data[j][i] == '#')


def neighbours(s, dim):
    if dim == 0:
        return []
    dim_nbs = []
    for i in [-1, 0, 1]:
        n = s[:dim-1] + (s[dim-1]+i,) + s[dim:]
        dim_nbs.append(n)
        dim_nbs += neighbours(n, dim-1)
    return [n for n in dim_nbs if n != s]


def pass_time(state, dim):
    for t in range(6):
        new_state = set()
        nbs = defaultdict(int)
        for s in state:
            for n in neighbours(s, dim):
                nbs[n] += 1
        for n in nbs:
            if n in state:
                if nbs[n] == 2 or nbs[n] == 3:
                    new_state.add(n)
            else:
                if nbs[n] == 3:
                    new_state.add(n)
        state = new_state
    return len(state)


print(f'Day 18 part 1: {pass_time(state1, 3)}')
print(f'Day 18 part 2: {pass_time(state2, 4)}')
