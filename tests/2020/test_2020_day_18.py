from aoc_2020.day_18.part_1 import calculate, extract
from aoc_2020.day_18.part_1 import main as part_1_solution
from aoc_2020.day_18.part_2 import calculate as calculate_part_2
from aoc_2020.day_18.part_2 import custom_add_multiply
from aoc_2020.day_18.part_2 import main as part_2_solution

equations = [
    "1 + (2 * 3) + (4 * (5 + 6))",
    "2 * 3 + (4 * 5)",
    "5 + (8 * 3 + 9 + 3 * 4 * 3)",
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
]


def test_extract():
    expected_output = [2, "*", 3, "+", "(", 4, "*", 5, ")"]

    assert extract(equations[1]) == expected_output


def test_part_1_calculate_1():
    expressions = extract(equations[0])

    assert calculate(expressions, 0)[0] == 51


def test_part_1_calculate_2():
    expressions = extract(equations[1])

    assert calculate(expressions, 0)[0] == 26


def test_part_1_calculate_3():
    expressions = extract(equations[2])

    assert calculate(expressions, 0)[0] == 437


def test_part_1_calculate_4():
    expressions = extract(equations[3])

    assert calculate(expressions, 0)[0] == 12240


def test_part_1_calculate_5():
    expressions = extract(equations[4])

    assert calculate(expressions, 0)[0] == 13632


def test_part_1_solution():
    assert part_1_solution(equations) == 26386


def test_custom_add_multiply():
    expressions = [2, "*", 23]

    assert custom_add_multiply(expressions) == 46


def test_part_2_calculate_1():
    expressions = extract(equations[0])

    assert calculate_part_2(expressions, 0)[0] == 51


def test_part_2_calculate_2():
    expressions = extract(equations[1])

    assert calculate_part_2(expressions, 0)[0] == 46


def test_part_2_calculate_3():
    expressions = extract(equations[2])

    assert calculate_part_2(expressions, 0)[0] == 1445


def test_part_2_calculate_4():
    expressions = extract(equations[3])

    assert calculate_part_2(expressions, 0)[0] == 669060


def test_part_2_calculate_5():
    expressions = extract(equations[4])

    assert calculate_part_2(expressions, 0)[0] == 23340


def test_part_2_solution():
    assert part_2_solution(equations) == 693942
