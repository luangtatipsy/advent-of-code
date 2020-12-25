from aoc_2020.day_15.part_1 import main as part_1_solution
from aoc_2020.day_15.part_2 import main as part_2_solution


def test_part_1_solution_1():
    numbers = [0, 3, 6]

    assert part_1_solution(numbers) == 436


def test_part_1_solution_2():
    numbers = [1, 3, 2]

    assert part_1_solution(numbers) == 1


def test_part_1_solution_3():
    numbers = [2, 1, 3]

    assert part_1_solution(numbers) == 10


def test_part_1_solution_4():
    numbers = [1, 2, 3]

    assert part_1_solution(numbers) == 27


def test_part_1_solution_5():
    numbers = [2, 3, 1]

    assert part_1_solution(numbers) == 78


def test_part_1_solution_6():
    numbers = [3, 2, 1]

    assert part_1_solution(numbers) == 438


def test_part_1_solution_7():
    numbers = [3, 1, 2]

    assert part_1_solution(numbers) == 1836


def test_part_2_solution_1():
    numbers = [0, 3, 6]

    assert part_2_solution(numbers) == 175594


def test_part_2_solution_2():
    numbers = [1, 3, 2]

    assert part_2_solution(numbers) == 2578


def test_part_2_solution_3():
    numbers = [2, 1, 3]

    assert part_2_solution(numbers) == 3544142


def test_part_2_solution_4():
    numbers = [1, 2, 3]

    assert part_2_solution(numbers) == 261214


def test_part_2_solution_5():
    numbers = [2, 3, 1]

    assert part_2_solution(numbers) == 6895259


def test_part_2_solution_6():
    numbers = [3, 2, 1]

    assert part_2_solution(numbers) == 18


def test_part_2_solution_7():
    numbers = [3, 1, 2]

    assert part_2_solution(numbers) == 362
