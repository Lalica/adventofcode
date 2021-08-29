def crab_combat(p1, p2, recursive=False):
    p1_turns, p2_turns = [], []

    while p1 and p2:
        if p1 in p1_turns and p2 in p2_turns and recursive:
            return 1, p1
        p1_turns.append(p1[:])
        p2_turns.append(p2[:])

        c1, c2 = p1.pop(0), p2.pop(0)

        if len(p1) >= c1 and len(p2) >= c2 and recursive:
            round_winner, _ = crab_combat(p1[:c1], p2[:c2], recursive)
        else:
            round_winner = 1 if c1 > c2 else 2

        if round_winner == 1:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]

    winner = 1 if len(p2) == 0 else 2
    winner_cards = p1 if winner == 1 else p2
    return winner, winner_cards


def play_games(player1, player2):
    _, winner = crab_combat(player1[:], player2[:])
    score = sum([(i + 1) * e for i, e in enumerate(reversed(winner))])
    print(f'Day 22 part 1: {score}')

    _, winner = crab_combat(player1[:], player2[:], True)
    score = sum([(i + 1) * e for i, e in enumerate(reversed(winner))])
    print(f'Day 22 part 2: {score}')


with open('../inputs/22.txt') as f:
    p1, p2 = f.read().split('\n\n')
    p1 = list(map(int, p1.strip().split('\n')[1:]))
    p2 = list(map(int, p2.strip().split('\n')[1:]))

play_games(p1, p2)
