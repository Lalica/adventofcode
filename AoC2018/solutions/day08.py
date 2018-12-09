nodes = map(int, open("../inputs/08.txt").read().split())


def tree2(head, part):
    global nodes
    meta, indexes = 0, 0
    children = []
    for i in range(nodes[head]):
        children.append(tree2(head + 2, part))
    meta += sum(nodes[i + head + 2] for i in range(nodes[head + 1]))
    for i in range(nodes[head+1]):
        indexes += children[nodes[head + 2 + i] - 1] if nodes[head + 2 + i] <= nodes[head] else 0
    nodes = nodes[:head] + nodes[head + 2 + nodes[head + 1]:]

    return meta + sum(children) if part == 1 else indexes if indexes != 0 else meta


print("Day 8 part 1: " + str(tree2(0, 1)))
nodes = map(int, open("../inputs/08.txt").read().split())
print("Day 8 part 2: " + str(tree2(0, 2)))
