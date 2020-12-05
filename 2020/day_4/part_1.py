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


def is_required(field):
    return required_fields.get(field)


def is_exist(field):
    return field in required_fields


def is_valid_passport(passport):
    fields = passport.split()
    check_list = []

    for field in fields:
        key, value = field.split(":")
        if is_required(key) and is_exist(key):
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
