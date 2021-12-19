from aoc_2021.day_10.part_1 import check as part_1_solution
from aoc_2021.day_10.part_2 import check as part_2_solution

syntax_list = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


def test_part_1_solution():
    assert part_1_solution(syntax_list) == 26397


def test_part_2_solution():
    assert part_2_solution(syntax_list) == 288957
