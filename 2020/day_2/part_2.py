with open("input.txt") as f:
    passwords = [line.strip() for line in f.read().splitlines(False) if line.strip() != ""]


def is_valid(first_position, second_position, character, password):
    is_first_char_correct = password[first_position - 1] == character
    is_second_char_correct = password[second_position - 1] == character

    return (
        is_first_char_correct + is_second_char_correct == 1
    )  # Exactly one of these positions must contain the given letter


valid_count = 0
for line in passwords:
    _policy, password = line.split(":")
    _range, character = _policy.split(" ")
    lowest, highest = _range.split("-")

    valid_count += is_valid(
        int(lowest), int(highest), character.strip(), password.strip()
    )

print(valid_count)
