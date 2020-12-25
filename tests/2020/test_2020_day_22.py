from aoc_2020.day_22.part_1 import main as part_1_solution
from aoc_2020.day_22.part_2 import main as part_2_solution
from aoc_2020.day_22.part_2 import play

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


def test_play_part_2():
    p1_deck = [1, 2, 3]
    p2_deck = [3, 2, 1]
    visited = {(tuple(p1_deck), tuple(p2_deck))}

    assert play(p1_deck, p2_deck, visited) == (1, [1, 2, 3])


def test_part_2_solution():
    assert part_2_solution(p1_deck, p2_deck) == 291
