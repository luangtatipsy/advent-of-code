from aoc_2021.day_2.part_1 import dive as part_1_solution
from aoc_2021.day_2.part_2 import dive as part_2_solution

instructions = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def test_part_1_solution():
    assert part_1_solution(instructions) == 150


def test_part_2_solution():
    assert part_2_solution(instructions) == 900
