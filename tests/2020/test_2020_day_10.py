from aoc_2020.day_10.part_1 import count_differences
from aoc_2020.day_10.part_1 import main as part_1_solution
from aoc_2020.day_10.part_2 import main as part_2_solution

adapters_1 = """
16
10
15
5
1
11
7
19
6
12
4
"""

adapters_2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


adapters_1 = [
    int(adapter) for adapter in adapters_1.splitlines(False) if adapter.strip() != ""
]

adapters_2 = [
    int(adapter) for adapter in adapters_2.splitlines(False) if adapter.strip() != ""
]


def test_count_difference_1():
    assert count_differences(adapters_1) == {1: 7, 2: 0, 3: 5}


def test_count_difference_2():
    assert count_differences(adapters_2) == {1: 22, 2: 0, 3: 10}


def test_part_1_solution_1():
    expected_output = 7 * 5

    assert part_1_solution(adapters_1) == expected_output


def test_part_1_solution_2():
    expected_output = 22 * 10

    assert part_1_solution(adapters_2) == expected_output


def test_part_2_solution_1():
    assert part_2_solution(adapters_1) == 8


def test_part_2_solution_2():
    assert part_2_solution(adapters_2) == 19208
