from day_3.part_1 import encounter_tree_count as part_1_solution
from day_3.part_2 import main as part_2_solution

square_map = """
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
"""
square_map = [
    line.strip() for line in square_map.splitlines(False) if line.strip() != ""
]


def test_part_1_solution():
    assert part_1_solution(square_map) == 7


def test_part_2_solution():
    assert part_2_solution(square_map) == 336
