from day_22.part_1 import main as part_1_solution

decks = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""
p1_deck, p2_deck = [
    [int(card) for card in deck.splitlines() if card.strip().isdigit()]
    for deck in decks.split("\n\n")
]


def test_part_1_solution():
    assert part_1_solution(p1_deck, p2_deck) == 306
