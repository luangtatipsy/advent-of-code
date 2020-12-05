import re

RE_HCL = re.compile(r"^#[0-9a-f]{6}$")
RE_PID = re.compile(r"^\d{9}$")


def validate_byr(value):
    return len(str(value)) == 4 and (int(value) >= 1920 and int(value) <= 2002)


def validate_iyr(value):
    return len(str(value)) == 4 and (int(value) >= 2010 and int(value) <= 2020)


def validate_eyr(value):
    return len(str(value)) == 4 and (int(value) >= 2020 and int(value) <= 2030)


def validate_hgt(value):
    value = str(value).lower()
    is_valid = False

    def __validate(number, _min, _max):
        return number.isdigit() and int(number) >= _min and int(number) <= _max

    if value.endswith("cm"):
        is_valid = __validate(value[:-2], 150, 193)
    elif value.endswith("in"):
        is_valid = __validate(value[:-2], 59, 76)

    return is_valid


def validate_hcl(value):
    return bool(RE_HCL.match(value))


def validate_ecl(value):
    return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def validate_pid(value):
    return bool(RE_PID.match(value))


required_fields = {
    "byr": True,
    "iyr": True,
    "eyr": True,
    "hgt": True,
    "hcl": True,
    "ecl": True,
    "pid": True,
    "cid": False,
}

field_conditions = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid,
    "cid": lambda cid: True,
}


def is_required(field):
    return required_fields.get(field)


def is_exist(field):
    return field in required_fields


def is_valid_passport(passport):
    fields = passport.split()
    check_list = []

    for field in fields:
        key, value = field.split(":")
        if is_required(key) and is_exist(key) and field_conditions.get(key)(value):
            check_list.append(True)

    return all(check_list) and len(check_list) >= 7


def main(passports):
    valid_passport_count = 0

    for passport in passports:
        valid_passport_count += is_valid_passport(passport)

    return valid_passport_count


if __name__ == "__main__":
    with open("input.txt") as f:
        passports = [row.strip() for row in f.read().split("\n\n") if row.strip() != ""]

    valid_passport_count = main(passports)
    print(valid_passport_count)
