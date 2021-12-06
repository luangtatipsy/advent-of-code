from aoc_2021.day_6.part_1 import grow as part_1_solution
from aoc_2021.day_6.part_2 import grow as part_2_solution

internal_timers = [3, 4, 3, 1, 2]


def test_part_1_solution():

    assert part_1_solution(internal_timers) == 5934


def test_part_2_solution():
    assert part_2_solution(internal_timers) == 26984457539
