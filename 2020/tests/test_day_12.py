from collections import deque

from day_12.part_1 import main as part_1_solution
from day_12.part_1 import move, rotate
from day_12.part_2 import main as part_2_solution
from day_12.part_2 import move_to_waypoint, move_waypoint
from day_12.part_2 import rotate as rotate_path_2

nav_instructions = """
F10
N3
F7
R90
F11
"""

nav_instructions = [
    instruction.strip()
    for instruction in nav_instructions.splitlines(False)
    if instruction.strip() != ""
]


def test_move_to_east_for_10_steps():
    assert move("E", (0, 0), 10) == (10, 0)


def test_move_to_north_for_3_steps():
    assert move("N", (-10, 0), 3) == (-10, -3)


def test_rotate_left_90_degree():
    _directions = deque(["N", "E", "S", "W"])
    expected_directions = deque(["W", "N", "E", "S"])

    assert rotate(_directions, "L", 90) == expected_directions


def test_rotate_right_90_degree():
    _directions = deque(["N", "E", "S", "W"])
    expected_directions = deque(["E", "S", "W", "N"])

    assert rotate(_directions, "R", 90) == expected_directions


def test_rotate_left_180_degree():
    _directions = deque(["N", "E", "S", "W"])
    expected_directions = deque(["S", "W", "N", "E"])

    assert rotate(_directions, "L", 180) == expected_directions


def test_rotate_right_180_degree():
    _directions = deque(["N", "E", "S", "W"])
    expected_directions = deque(["S", "W", "N", "E"])

    assert rotate(_directions, "R", 180) == expected_directions


def test_move_to_waypoint():
    expected_waypoint = (100, -10)

    assert (
        move_to_waypoint(waypoint=(10, -1), coordinate=(0, 0), steps=10)
        == expected_waypoint
    )


def test_move_waypoint_to_north_for_3():
    expected_waypoint = (10, -4)

    assert move_waypoint(direction="N", waypoint=(10, -1), steps=3) == expected_waypoint


def test_move_waypoint_to_east_for_3():
    expected_waypoint = (13, -1)

    assert move_waypoint(direction="E", waypoint=(10, -1), steps=3) == expected_waypoint


def test_rotate_part_2():
    assert rotate_path_2((0, 0), (10, -4), 90) == (4, 10)


def test_part_1_solution():
    assert part_1_solution(nav_instructions) == 25


def test_part_2_solution():
    assert part_2_solution(nav_instructions) == 286
