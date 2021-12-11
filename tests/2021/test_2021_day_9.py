from aoc_2021.day_9.part_1 import explore as part_1_solution
from aoc_2021.day_9.part_2 import explore as part_2_solution

signals = ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]


def test_part_1_solution():
    assert part_1_solution(signals) == 15


def test_part_2_solution():
    assert part_2_solution(signals) == 1134
