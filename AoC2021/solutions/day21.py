from functools import cache


@cache
def play_game(active_pos, pasive_pos, active_score=0, pasive_score=0):
    if pasive_score >= 21:
        return [0, 1]

    universes_won = [0, 0]
    for dice_sum_, num in sum_combinations:
        new_pos = (active_pos - 1 + dice_sum_) % 10 + 1
        new_score = active_score + new_pos

        p2_win, p1_win = play_game(pasive_pos, new_pos, pasive_score, new_score)

        universes_won[0] += p1_win * num
        universes_won[1] += p2_win * num

    return universes_won


def play_practice(start1, start2):
    pos = [start1, start2]
    score = [0, 0]
    deterministic_die = 1
    die_rolled = 0
    while True:
        for i in range(2):
            pos[i] = (pos[i] - 1 + deterministic_die * 3 + 3) % 10 + 1
            score[i] += pos[i]
            deterministic_die = (deterministic_die - 1 + 3) % 100 + 1
            die_rolled += 3

            if score[i] >= 1000:
                return score[(i + 1) % 2] * die_rolled


with open("../inputs/21.txt") as f:
    start1, start2 = list(map(lambda x: int(x[-2]), f))

print(f"Day 21 part 1: {play_practice(start1, start2)}")

sum_combinations = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]
print(f"Day 21 part 2: {max(play_game(start1, start2))}")
