from aoc_2021.day_7.part_1 import consume_fuel as part_1_solution
from aoc_2021.day_7.part_2 import consume_fuel as part_2_solution

positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_part_1_solution():

    assert part_1_solution(positions) == 37


def test_part_2_solution():
    assert part_2_solution(positions) == 168
