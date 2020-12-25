from aoc_2020.day_9.part_1 import find_invalid_number as part_1_solution
from aoc_2020.day_9.part_2 import main as part_2_solution

numbers = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

numbers = [int(number) for number in numbers.splitlines(False) if number.strip() != ""]


def test_part_1_solution():
    assert part_1_solution(numbers, volume=5) == 127


def test_part_2_solution():
    assert part_2_solution(numbers, volume=5) == 62

