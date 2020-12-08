from day_8.part_1 import extract
from day_8.part_1 import main as part_1_solution
from day_8.part_2 import find_operation_indice, generate
from day_8.part_2 import main as part_2_solution
from day_8.part_2 import restructure, switch

instructions = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

instructions = [
    instruction.strip()
    for instruction in instructions.splitlines(False)
    if instruction.strip() != ""
]


def test_extract():
    expected_instruction = ("nop", 0)

    assert extract(instructions[0]) == expected_instruction


def test_part_1_solution():
    assert part_1_solution(instructions) == 5


def test_restructure():
    _instructions = ["nop +0", "acc +1"]
    expected_instructions = [
        ("nop", 0),
        ("acc", 1),
    ]

    assert restructure(_instructions) == expected_instructions


def test_find_operation_indice():
    _instructions = [
        ("nop", 0),
        ("acc", 1),
        ("jmp", 99),
    ]
    expected_indice = [0, 2]

    assert find_operation_indice(_instructions) == expected_indice


def test_switch_1():
    _operation = "nop"
    expected_operation = "jmp"

    assert switch(_operation) == expected_operation


def test_switch_2():
    _operation = "jmp"
    expected_operation = "nop"

    assert switch(_operation) == expected_operation


def test_generate():
    _instructions = [
        ("nop", 0),
        ("acc", 1),
        ("jmp", 99),
    ]
    _indice = [0, 2]

    expected_instructions = [
        [("jmp", 0), ("acc", 1), ("jmp", 99)],
        [("nop", 0), ("acc", 1), ("nop", 99)],
    ]

    assert generate(_instructions, _indice) == expected_instructions


def test_part_2_solution():
    assert part_2_solution(instructions) == 8
