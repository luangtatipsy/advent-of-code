from aoc_2021.day_5.part_1 import hydrothermal_venture as part_1_solution
from aoc_2021.day_5.part_2 import hydrothermal_venture as part_2_solution

vents = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


def test_part_1_solution():

    assert part_1_solution(vents) == 5


def test_part_2_solution():
    assert part_2_solution(vents) == 12
