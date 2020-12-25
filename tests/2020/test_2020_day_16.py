from aoc_2020.day_16.part_1 import extract, extract_numbers, extract_range
from aoc_2020.day_16.part_1 import main as part_1_solution

# from aoc_2020.day_16.part_2 import main as part_2_solution

notes = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

notes = [note.strip() for note in notes.splitlines(False) if note.strip() != ""]


def test_extract():
    rules = ["class: 1-3 or 5-7", "row: 6-11 or 33-44", "seat: 13-40 or 45-50"]
    numbers_on_ticket = ["7,1,14"]
    numbers_on_nearby_tickets = ["7,3,47", "40,4,50", "55,2,20", "38,6,12"]

    assert extract(notes) == (rules, numbers_on_ticket, numbers_on_nearby_tickets)


def test_extract_range():
    _rules = ["class: 1-3 or 5-7"]
    expected_ranges = [1, 2, 3, 5, 6, 7]

    assert extract_range(_rules) == expected_ranges


def test_extract_numbers():
    _numbers_on_ticket = ["7,1,14"]
    expected_numbers = [[7, 1, 14]]

    assert extract_numbers(_numbers_on_ticket) == expected_numbers


def test_part_1_solution_1():
    assert part_1_solution(notes) == 71
