from aoc_2020.day_4.part_1 import main as part_1_solution
from aoc_2020.day_4.part_2 import is_valid_passport
from aoc_2020.day_4.part_2 import main as part_2_solution
from aoc_2020.day_4.part_2 import (
    validate_byr,
    validate_ecl,
    validate_eyr,
    validate_hcl,
    validate_hgt,
    validate_iyr,
    validate_pid,
)

passports = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm

    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in
"""
passports = [line.strip() for line in passports.split("\n\n") if line.strip() != ""]


def test_part_1_solution():
    assert part_1_solution(passports) == 2


def test_validate_byr_valid():
    assert validate_byr("2002") == True


def test_validate_byr_invalid():
    assert validate_byr("2003") == False


def test_validate_ecl_valid():
    assert validate_ecl("brn") == True


def test_validate_ecl_invalid():
    assert validate_ecl("wat") == False


def test_validate_eyr_valid():
    assert validate_eyr("2020") == True


def test_validate_eyr_invalid():
    assert validate_eyr("2031") == False


def test_validate_hcl_valid():
    assert validate_hcl("#123abc") == True


def test_validate_hcl_invalid():
    assert validate_hcl("#123abz") == False


def test_validate_hcl_invalid_for_missing_number_sign():
    assert validate_hcl("123abc") == False


def test_validate_hcl_invalid_for_too_long_more_than_six_characters_length():
    assert validate_hcl("#123abcaaaaa") == False


def test_validate_hcl_invalid_for_too_short_less_than_six_characters_length():
    assert validate_hcl("#123") == False


def test_validate_hgt_valid_for_in_case():
    assert validate_hgt("60in") == True


def test_validate_hgt_valid_for_cm_case():
    assert validate_hgt("190cm") == True


def test_validate_hgt_invalid_for_in_case():
    assert validate_hgt("190in") == False


def test_validate_hgt_invalid_for_cm_case():
    assert validate_hgt("149cm") == False


def test_validate_hgt_invalid_for_missing_unit():
    assert validate_hgt("190") == False


def test_validate_iyr_valid():
    assert validate_iyr("2020") == True


def test_validate_iyr_invalid():
    assert validate_iyr("2031") == False


def test_validate_pid_valid():
    assert validate_pid("000000001") == True


def test_validate_pid_invalid_for_not_exactly_nine_digit_number():
    assert validate_pid("0123456789") == False


def test_invalid_passport_1():
    passport = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"""

    assert is_valid_passport(passport) == False


def test_invalid_passport_2():
    passport = """iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946"""

    assert is_valid_passport(passport) == False


def test_invalid_passport_3():
    passport = """hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"""

    assert is_valid_passport(passport) == False


def test_invalid_passport_4():
    passport = """hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

    assert is_valid_passport(passport) == False


def test_valid_passport_1():
    passport = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f"""

    assert is_valid_passport(passport) == True


def test_valid_passport_2():
    passport = """eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"""

    assert is_valid_passport(passport) == True


def test_valid_passport_3():
    passport = """hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022"""

    assert is_valid_passport(passport) == True


def test_valid_passport_4():
    passport = (
        """iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
    )

    assert is_valid_passport(passport) == True


def test_part_2_solution():
    assert part_2_solution(passports) == 2
