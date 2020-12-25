from aoc_2020.day_5.part_1 import extract_seat_id
from aoc_2020.day_5.part_1 import main as part_1_solution

# Part 2 solution does not change core program logic then, it's not necessary to test it


boarding_passes = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def test_extract_seat_id_1():
    boarding_pass = boarding_passes[0]
    assert extract_seat_id(boarding_pass) == 357


def test_extract_seat_id_2():
    boarding_pass = boarding_passes[1]
    assert extract_seat_id(boarding_pass) == 567


def test_extract_seat_id_3():
    boarding_pass = boarding_passes[2]
    assert extract_seat_id(boarding_pass) == 119


def test_extract_seat_id_4():
    boarding_pass = boarding_passes[3]
    assert extract_seat_id(boarding_pass) == 820


def test_part_1_solution():
    assert part_1_solution(boarding_passes) == 820
