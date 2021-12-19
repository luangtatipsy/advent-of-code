from aoc_2021.day_14.part_1 import polymerize as part_1_solution
from aoc_2021.day_14.part_2 import polymerize as part_2_solution

(
    template,
    instructions,
) = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".split(
    "\n\n"
)

insertion_pair = {}
for instruction in instructions.split("\n"):
    pair, insertion = instruction.split(" -> ")
    insertion_pair[pair] = insertion


def test_part_1_solution():
    assert part_1_solution(template, insertion_pair) == 1588


def test_part_2_solution():
    assert part_2_solution(template, insertion_pair) == 2188189693529
