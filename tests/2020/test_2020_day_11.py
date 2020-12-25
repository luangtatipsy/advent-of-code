from aoc_2020.day_11.part_1 import look_around
from aoc_2020.day_11.part_1 import main as part_1_solution
from aoc_2020.day_11.part_1 import sit_or_stand
from aoc_2020.day_11.part_2 import look_around as look_around_part_2
from aoc_2020.day_11.part_2 import main as part_2_solution

seat_layout = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

seat_layout = [
    line.strip() for line in seat_layout.splitlines(False) if line.strip() != ""
]


def test_look_around_1():
    assert look_around(0, 0, seat_layout) == 0


def test_look_around_2():
    _seat_layout = ["L.LL.LL.LL", "LL#LLLL.LL"]

    assert look_around(2, 0, _seat_layout) == 1


def test_sit_or_stand_for_sit():
    expected_layout = [
        "#.##.##.##",
        "#######.##",
        "#.#.#..#..",
        "####.##.##",
        "#.##.##.##",
        "#.#####.##",
        "..#.#.....",
        "##########",
        "#.######.#",
        "#.#####.##",
    ]

    assert sit_or_stand(seat_layout, activity="sit") == expected_layout


def test_sit_or_stand_for_stand():
    expected_layout = [
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL",
    ]

    assert sit_or_stand(seat_layout, activity="stand") == expected_layout


def test_part_1_solution():
    assert part_1_solution(seat_layout) == 37


def test_look_around_part_2_1():
    _layout = [
        ".......#.",
        "...#.....",
        ".#.......",
        ".........",
        "..#L....#",
        "....#....",
        ".........",
        "#........",
        "...#.....",
    ]

    assert look_around_part_2(3, 4, _layout) == 8


def test_look_around_part_2_2():
    _layout = [
        ".............",
        ".L.L.#.#.#.#.",
        ".............",
    ]

    assert look_around_part_2(1, 1, _layout) == 0


def test_look_around_part_2_3():
    _layout = [
        ".##.##.",
        "#.#.#.#",
        "##...##",
        "...L...",
        "##...##",
        "#.#.#.#",
        ".##.##.",
    ]
    assert look_around_part_2(3, 3, _layout) == 0


def test_part_2_solution():
    assert part_2_solution(seat_layout) == 26
