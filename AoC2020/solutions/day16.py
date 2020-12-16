with open('../inputs/16.txt') as f:
    ruless, my_ticket, tickets = f.read().strip().split('\n\n')

    rules = dict()
    for rule in ruless.split('\n'):
        a, b = rule.split(':')
        rules[a] = [[int(x) for x in r.split('-')] for r in b.split(' or ')]

    my_ticket = list(map(int, my_ticket.split('\n')[1].split(',')))
    tickets = [list(map(int, ticket.split(','))) for ticket in tickets.split('\n')[1:]]


def valid(num):
    for rule in rules.values():
        if rule_valid(num, rule):
            return True
    return False


def rule_valid(num, rule):
    for a, b in rule:
        if a <= num <= b:
            return True
    return False


error = 0
valid_tickets = []
for ticket in tickets:
    flag = True
    for t in ticket:
        if not valid(t):
            error += t
            flag = False
    if flag:
        valid_tickets.append(ticket)

n = len(tickets[0])
rule_order = [set() for _ in range(n)]
all_rules, rules_done = set(rules.keys()), set()
for i in range(n):
    for rule in all_rules - rules_done:
        if all(rule_valid(vt[i], rules[rule]) for vt in valid_tickets):
            rule_order[i].add(rule)
    if len(rule_order[i]) == 1:
        rules_done = rules_done.union(rule_order[i])

while len(rules_done) < 20:
    for i in range(n):
        if len(rule_order[i]) != 1:
            rule_order[i] -= rules_done
            if len(rule_order[i]) == 1:
                rules_done = rules_done.union(rule_order[i])

part2 = 1
for i in range(n):
    if 'departure' in rule_order[i].pop():
        part2 *= my_ticket[i]

print(f'Day 16 part 1: {error}')
print(f'Day 16 part 2: {part2}')
