from day_5.part_1 import extract_seat_id as part_1_solution

# Part 2 solution does not change core program logic then, it's not necessary to test it


def test_part_1_solution_1():
    boarding_pass = "FBFBBFFRLR"
    assert part_1_solution(boarding_pass) == 357


def test_part_1_solution_2():
    boarding_pass = "BFFFBBFRRR"
    assert part_1_solution(boarding_pass) == 567


def test_part_1_solution_3():
    boarding_pass = "FFFBBBFRRR"
    assert part_1_solution(boarding_pass) == 119


def test_part_1_solution_4():
    boarding_pass = "BBFFBBFRLL"
    assert part_1_solution(boarding_pass) == 820

