from aoc_2021.day_1.part_1 import count_increased_measurements as part_1_solution
from aoc_2021.day_1.part_2 import (
    count_three_measurement_sliding_window as part_2_solution,
)

depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part_1_solution():
    assert part_1_solution(depths) == 7


def test_part_2_solution():
    assert part_2_solution(depths) == 5
