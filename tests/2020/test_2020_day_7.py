from aoc_2020.day_7.part_1 import extract
from aoc_2020.day_7.part_1 import main as part_1_solution
from aoc_2020.day_7.part_2 import main as part_2_solution

rules = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

rules_part_2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

rules = [rule.strip() for rule in rules.splitlines(False) if rule.strip() != ""]
rules_part_2 = [
    rule.strip() for rule in rules_part_2.splitlines(False) if rule.strip() != ""
]


def test_extract_rule_1():
    expected_rule = ("light red", {"bright white": 1, "muted yellow": 2})

    assert extract(rules[0]) == expected_rule


def test_extract_rule_2():
    expected_rule = ("dark orange", {"bright white": 3, "muted yellow": 4})

    assert extract(rules[1]) == expected_rule


def test_extract_rule_3():
    expected_rule = ("bright white", {"shiny gold": 1})

    assert extract(rules[2]) == expected_rule


def test_extract_rule_4():
    expected_rule = ("muted yellow", {"shiny gold": 2, "faded blue": 9})

    assert extract(rules[3]) == expected_rule


def test_extract_rule_5():
    expected_rule = ("shiny gold", {"dark olive": 1, "vibrant plum": 2})

    assert extract(rules[4]) == expected_rule


def test_extract_rule_6():
    expected_rule = ("dark olive", {"faded blue": 3, "dotted black": 4})

    assert extract(rules[5]) == expected_rule


def test_extract_rule_7():
    expected_rule = ("vibrant plum", {"faded blue": 5, "dotted black": 6})

    assert extract(rules[6]) == expected_rule


def test_extract_rule_8():
    expected_rule = ("faded blue", {})

    assert extract(rules[7]) == expected_rule


def test_extract_rule_9():
    expected_rule = ("dotted black", {})

    assert extract(rules[8]) == expected_rule


def test_part_1_solution():
    assert part_1_solution(rules) == 4


def test_part_2_solution_1():
    assert part_2_solution(rules) == 32


def test_part_2_solution():
    assert part_2_solution(rules_part_2) == 126
