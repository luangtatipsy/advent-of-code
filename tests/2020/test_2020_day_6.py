from aoc_2020.day_6.part_1 import count_survey_for_anyone
from aoc_2020.day_6.part_1 import main as part_1_solution
from aoc_2020.day_6.part_2 import count_survey_for_everyone
from aoc_2020.day_6.part_2 import main as part_2_solution

surveys = """abc

a
b
c

ab
ac

a
a
a
a

b"""

surveys = [survey.strip() for survey in surveys.split("\n\n") if survey.strip() != ""]


def test_count_survey_for_anyone_1():
    survey = """abcx
abcy
abcz"""
    assert count_survey_for_anyone(survey) == 6


def test_count_survey_for_anyone_2():
    survey = surveys[0]
    assert count_survey_for_anyone(survey) == 3


def test_count_survey_for_anyone_3():
    survey = surveys[1]
    assert count_survey_for_anyone(survey) == 3


def test_count_survey_for_anyone_4():
    survey = surveys[2]
    assert count_survey_for_anyone(survey) == 3


def test_count_survey_for_anyone_5():
    survey = surveys[3]
    assert count_survey_for_anyone(survey) == 1


def test_count_survey_for_anyone_6():
    survey = surveys[4]
    assert count_survey_for_anyone(survey) == 1


def test_part_1_solution():
    assert part_1_solution(surveys) == 11


def test_count_survey_for_everyone_1():
    survey = """abcx
abcy
abcz"""
    assert count_survey_for_everyone(survey) == 3


def test_count_survey_for_everyone_2():
    survey = surveys[0]
    assert count_survey_for_everyone(survey) == 3


def test_count_survey_for_everyone_3():
    survey = surveys[1]
    assert count_survey_for_everyone(survey) == 0


def test_count_survey_for_everyone_4():
    survey = surveys[2]
    assert count_survey_for_everyone(survey) == 1


def test_count_survey_for_everyone_5():
    survey = surveys[3]
    assert count_survey_for_everyone(survey) == 1


def test_count_survey_for_everyone_6():
    survey = surveys[4]
    assert count_survey_for_everyone(survey) == 1


def test_part_2_solution():
    assert part_2_solution(surveys) == 6
