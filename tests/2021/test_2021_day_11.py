from aoc_2021.day_11.part_1 import measure as part_1_solution
from aoc_2021.day_11.part_2 import measure as part_2_solution

_octopuses = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
octopuses = [[int(octopus) for octopus in line] for line in _octopuses.split("\n")]


def test_part_1_solution():
    assert part_1_solution(octopuses) == 1656


def test_part_2_solution():
    assert part_2_solution(octopuses) == 195
