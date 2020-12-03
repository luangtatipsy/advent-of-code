with open("input.txt") as f:
    passwords = [line.strip() for line in f.read().splitlines(False) if line.strip() != ""]


def is_valid(lowest, highest, character, password):
    num_occurrences = password.count(character)

    return num_occurrences >= lowest and num_occurrences <= highest


valid_count = 0
for line in passwords:
    _policy, password = line.split(":")
    _range, character = _policy.split(" ")
    lowest, highest = _range.split("-")

    valid_count += is_valid(
        int(lowest), int(highest), character.strip(), password.strip()
    )

print(valid_count)
