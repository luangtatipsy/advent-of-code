def play(p1_deck, p2_deck, visited):
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        if (tuple(p1_deck), tuple(p2_deck)) in visited:
            return 1, p1_deck

        visited.add((tuple(p1_deck), tuple(p2_deck)))

        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)

        if len(p1_deck) >= p1_card and len(p2_deck) >= p2_card:
            winner, _ = play(p1_deck[:p1_card], p2_deck[:p2_card], set())
        else:
            winner = 1 if p1_card > p2_card else 2

        if winner == 1:
            p1_deck.extend([p1_card, p2_card])
        else:
            p2_deck.extend([p2_card, p1_card])

    return (1, p1_deck) if len(p1_deck) > 2 else (2, p2_deck)


def main(p1_deck, p2_deck):
    _, deck = play(p1_deck, p2_deck, set())

    score = 0
    for card, order in zip(deck, range(len(deck), 0, -1)):
        score += card * order

    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        p1_deck, p2_deck = [
            [int(card) for card in deck.splitlines() if card.strip().isdigit()]
            for deck in f.read().split("\n\n")
        ]

    score = main(p1_deck, p2_deck)
    print(score)
