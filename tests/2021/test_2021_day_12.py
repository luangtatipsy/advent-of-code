from aoc_2021.day_12.part_1 import traverse as part_1_solution
from aoc_2021.day_12.part_2 import traverse as part_2_solution

paths = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
]


def test_part_1_solution():
    assert part_1_solution(paths) == 19


def test_part_2_solution():
    assert part_2_solution(paths) == 103
