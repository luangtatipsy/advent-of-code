from day_2.part_1 import main as part_1_solution
from day_2.part_2 import main as part_2_solution

passwords = """
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
"""
passwords = [line.strip() for line in passwords.splitlines(False) if line.strip() != ""]


def test_part_1_solution():
    assert part_1_solution(passwords) == 2


def test_part_2_solution():
    assert part_2_solution(passwords) == 1
