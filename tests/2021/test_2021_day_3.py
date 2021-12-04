from aoc_2021.day_3.part_1 import binary_diagnostic as part_1_solution
from aoc_2021.day_3.part_2 import life_support_rating as part_2_solution

diagnostic_reports = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_part_1_solution():
    assert part_1_solution(diagnostic_reports) == 198


def test_part_2_solution():
    assert part_2_solution(diagnostic_reports) == 230
