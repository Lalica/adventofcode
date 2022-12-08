from collections import defaultdict


class Game(object):
    def __init__(self, initial_boss, hard_mode=False):
        self.initial_boss = initial_boss
        self.spells = {
            "magic_missile": {"name": "magic_missile", "cost": 53, "spell": self.magic_missile},
            "drain": {"name": "drain", "cost": 73, "spell": self.drain},
            "shield": {"name": "shield", "cost": 113, "turns": 6, "spell": lambda x: self.effect(x), "effect": self.shield},
            "poison": {"name": "poison", "cost": 173, "turns": 6, "spell": lambda x: self.effect(x), "effect": self.poison},
            "recharge": {"name": "recharge", "cost": 229, "turns": 5, "spell": lambda x: self.effect(x), "effect": self.recharge},
        }
        self.reset()
        self.hard_mode = hard_mode

    def reset(self):
        self.hp, self.mana = 50, 500
        self.boss_hp, self.boss_attack = self.initial_boss
        self.active_effects = dict()

    def game_state(self):
        return tuple([self.hp, self.mana, self.boss_hp, frozenset(tuple([name, self.active_effects[name]["turns"]]) for name in self.active_effects)])

    def end_condition(self):
        return self.boss_hp <= 0 or self.hp <= 0

    def winner(self):
        return self.boss_hp <= 0

    def magic_missile(self, _):
        self.boss_hp -= 4

    def drain(self, _):
        self.boss_hp -= 2
        self.hp += 2

    def shield(self):
        self.defend = 7

    def poison(self):
        self.boss_hp -= 3

    def recharge(self):
        self.mana += 101

    def effect(self, spell):
        self.active_effects[spell["name"]] = spell.copy()

    def activate_effects(self):
        to_remove = []
        for effect in self.active_effects.values():
            effect["effect"]()

            effect["turns"] -= 1
            if effect["turns"] == 0:
                to_remove.append(effect["name"])

        for effect in to_remove:
            del self.active_effects[effect]

    def can_cast(self, spell):
        return spell not in self.active_effects and self.spells[spell]["cost"] <= self.mana

    def cast(self, spell_name):
        spell = self.spells[spell_name]
        spell["spell"](spell)
        self.mana -= spell["cost"]
        return spell["cost"]

    def make_move(self, spell):
        if self.hard_mode:
            self.hp -= 1
            if self.end_condition():
                return self.winner(), 0

        self.defend = 0
        self.activate_effects()
        if self.end_condition():
            return self.winner(), 0

        if not self.can_cast(spell):
            return None, -1

        mana_cost = self.cast(spell)
        if self.end_condition():
            return self.winner(), mana_cost

        self.defend = 0
        self.activate_effects()
        if self.end_condition():
            return self.winner(), mana_cost

        self.hp -= max(1, self.boss_attack - self.defend)
        if self.end_condition():
            return self.winner(), mana_cost

        return None, mana_cost

    def set_game(self, game_state):
        self.hp = game_state[0]
        self.mana = game_state[1]
        self.boss_hp = game_state[2]
        self.active_effects = dict()
        for name, turns in game_state[3]:
            self.active_effects[name] = self.spells[name].copy()
            self.active_effects[name]["turns"] = turns


def dijkstra(start_node, game, verbose=False):
    visited, to_visit = set(), [start_node]
    shortest_path = defaultdict(lambda: float("inf"))
    shortest_path[start_node] = 0
    spell_path = dict()
    spell_path[start_node] = ""

    while to_visit:
        node = to_visit.pop(0)

        visited.add(node)

        game.set_game(node)
        mana_spent_before = shortest_path[node]

        for spell in game.spells:
            winner, mana_cost = game.make_move(spell)
            if mana_cost == -1:
                game.set_game(node)
                continue

            mana_spent = mana_spent_before + mana_cost

            if winner is None:
                nbr_node = game.game_state()
                if nbr_node not in visited and mana_spent < shortest_path[nbr_node]:
                    shortest_path[nbr_node] = mana_spent
                    spell_path[nbr_node] = spell_path[node] + spell + " "

                    to_visit.append(nbr_node)
                    to_visit.sort(key=lambda x: shortest_path[x])
            elif winner:
                if verbose:
                    print(spell_path[node] + spell + " ")
                return mana_spent

            game.set_game(node)

    return -1


with open("../inputs/22.txt") as f:
    initial_boss = [int(line.split(": ")[1]) for line in f]

game = Game(initial_boss)
part1 = dijkstra(game.game_state(), game)
print(f"Day 22 part 1: {part1}")

game = Game(initial_boss, True)
part2 = dijkstra(game.game_state(), game)
print(f"Day 22 part 2: {part2}")
