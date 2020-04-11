from copy import deepcopy
from operator import attrgetter


class Group:
    def __init__(self, units, hit_points, immune, weak,
                 damage, damage_type, boosted, initiative):
        self.units = units
        self.hit_points = hit_points
        self.immune = immune
        self.weak = weak
        self.damage = damage
        self.damage_type = damage_type
        self.boosted = boosted
        self.initiative = initiative
        self.target = ''

    def __repr__(self):
        return str(vars(self)) + '\n'

    @property
    def ep(self):
        return self.units * (self.damage + (boost if self.boosted else 0))


def read(army_data, boosted):
    army = dict()
    for data in army_data:
        d = data.split()
        traits = ' '.join(d[7:-11])[1:-1].replace(',', '').split('; ')
        traits = [] if '' in traits else traits
        traits_dict = {k: v for k, _, *v in map(str.split, traits)}

        army[int(d[-1])] = Group(units=int(d[0]),
                                 hit_points=int(d[4]),
                                 immune=traits_dict.get('immune', []),
                                 weak=traits_dict.get('weak', []),
                                 damage=int(d[-6]),
                                 damage_type=d[-5],
                                 boosted=boosted,
                                 initiative=int(d[-1]))
    return army


def damage(attacker, target):
    damage_multiplier = 1
    if attacker.damage_type in target.immune:
        damage_multiplier = 0
    if attacker.damage_type in target.weak:
        damage_multiplier = 2
    return attacker.ep * damage_multiplier


def get_group(army1, army2, i):
    group = army1.get(i, None)
    if group is None:
        group = army2.get(i, None)
    return group


def find_targets(allies, enemies):
    targeted = []
    for group in sorted(allies.values(),
                        key=attrgetter('ep', 'initiative'),
                        reverse=True):
        if len(targeted) == len(enemies):
            break
        enemy = sorted([g for g in enemies if g.initiative not in targeted],
                       key=lambda x: (damage(group, x), x.ep, x.initiative),
                       reverse=True)[0]
        if group.damage_type in enemy.immune:
            continue
        group.target = enemy.initiative
        allies[group.initiative] = group
        targeted.append(enemy.initiative)
    return allies


def battle(army1, army2):
    someone_died = False
    for i in range(max_initiative, 0, -1):
        attacker = get_group(army1, army2, i)
        if attacker is None or attacker.target == '':
            continue
        target = get_group(army1, army2, attacker.target)
        dead = damage(attacker, target) // target.hit_points
        if dead:
            someone_died = True
        target.units -= dead
        if target.units <= 0:
            if target.initiative in army1:
                del army1[target.initiative]
            else:
                del army2[target.initiative]
        attacker.target = ''
    return army1, army2, someone_died


with open('../inputs/24.txt') as f:
    army1, army2 = f.read().strip().split('\n\n')
    ims = read(army1.split('\n')[1:], True)
    inf = read(army2.split('\n')[1:], False)
    max_initiative = max(*[g.initiative for g in ims.values()],
                         *[g.initiative for g in inf.values()])
    boost = 0

    while True:
        immune_system, infection = deepcopy(ims), deepcopy(inf)
        not_tie = True
        while immune_system and infection and not_tie:
            immune_system = find_targets(immune_system, infection.values())
            infection = find_targets(infection, immune_system.values())
            immune_system, infection, not_tie = battle(immune_system, infection)

        if not boost:
            army = immune_system.values() if immune_system else infection.values()
            print(sum(group.units for group in army))
        if immune_system and not_tie:
            print(sum(group.units for group in immune_system.values()))
            break
        boost += 1
