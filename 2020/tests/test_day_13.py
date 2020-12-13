from day_13.part_1 import main as part_1_solution
from day_13.part_2 import main as part_2_solution

notes = """
939
7,13,x,x,59,x,31,19
"""

notes = [note.strip() for note in notes.splitlines(False) if note.strip() != ""]


def test_part_1_solution():
    assert part_1_solution(notes) == 295


def test_part_2_solution_1():
    assert part_2_solution(notes) == 1068781


def test_part_2_solution_2():
    notes = ["939", "17,x,13,19"]

    assert part_2_solution(notes) == 3417


def test_part_2_solution_3():
    notes = ["939", "67,7,59,61"]

    assert part_2_solution(notes) == 754018


def test_part_2_solution_4():
    notes = ["939", "67,x,7,59,61"]

    assert part_2_solution(notes) == 779210


def test_part_2_solution_5():
    notes = ["939", "67,7,x,59,61"]

    assert part_2_solution(notes) == 1261476


def test_part_2_solution_6():
    notes = ["939", "1789,37,47,1889"]

    assert part_2_solution(notes) == 1202161486
