from aoc_2019.day_2.part_1 import main as part_1_solution
from aoc_2019.day_2.part_2 import main as part_2_solution

sequence = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_part_1_solution():
    assert part_1_solution(sequence) == 3500


def test_part_2_solution():
    # It is a brute force problem, therefore it has to be tested with the full puzzle input
    with open("aoc_2019/day_2/input.txt") as f:
        sequence = [int(number) for number in f.read().split(",")]

    assert part_2_solution(sequence) == 7960
