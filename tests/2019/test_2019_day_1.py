from aoc_2019.day_1.part_1 import calculate
from aoc_2019.day_1.part_1 import main as part_1_solution
from aoc_2019.day_1.part_2 import main as part_2_solution

masses = [12, 14, 1969, 100756]


def test_calculate_1():
    mass = 12
    assert calculate(mass) == 2


def test_calculate_2():
    mass = 14
    assert calculate(mass) == 2


def test_calculate_3():
    mass = 1969
    assert calculate(mass) == 654


def test_calculate_4():
    mass = 100756
    assert calculate(mass) == 33583


def test_part_1_solution():
    assert part_1_solution(masses) == 34241


def test_part_2_solution():
    assert part_2_solution(masses) == 51316
