def is_valid(lowest, highest, character, password):
    num_occurrences = password.count(character)

    return num_occurrences >= lowest and num_occurrences <= highest

def extract_policy(line):
    _policy, password = line.split(":")
    _range, character = _policy.split(" ")
    lowest, highest = _range.split("-")

    return int(lowest), int(highest), character.strip(), password.strip()


def main(passwords):
    valid_count = 0
    for line in passwords:
        lowest, highest, character, password = extract_policy(line)
        valid_count += is_valid(lowest, highest, character, password)

    return valid_count

if __name__ == "__main__":    
    with open("input.txt") as f:
        passwords = [line.strip() for line in f.read().splitlines(False) if line.strip() != ""]

    valid_count = main(passwords)
    print(valid_count)
