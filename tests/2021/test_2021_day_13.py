from aoc_2021.day_13.part_1 import fold as part_1_solution

# part 2 solution is not testable

(
    points_str,
    instructions_str,
) = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".split(
    "\n\n"
)

points = set(tuple(map(int, line.split(","))) for line in points_str.splitlines(False))
instructions = []
for instruction in instructions_str.splitlines(False):
    axis_ins, fold_pos = instruction.split("=")
    axis = axis_ins[-1]
    instructions.append({axis: int(fold_pos)})


def test_part_1_solution():
    assert part_1_solution(points, instructions) == 17
