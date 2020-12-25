import re

RANGE_RE = re.compile(r"[a-z:]")


def extract(notes):
    ticket_index = notes.index("your ticket:")
    nearby_ticket_index = notes.index("nearby tickets:")

    rules = notes[:ticket_index]
    my_ticket = notes[ticket_index + 1 : nearby_ticket_index]
    nearby_tickets = notes[nearby_ticket_index + 1 :]

    return rules, my_ticket, nearby_tickets


def extract_range(rules):
    ranges = []
    for rule in rules:
        for _range in RANGE_RE.sub("", rule).split(" "):
            if _range.strip() != "":
                _min, _max = _range.split("-")
                ranges.extend(range(int(_min), int(_max) + 1))

    return ranges


def extract_numbers(numbers_text):
    return [list(map(int, text.split(","))) for text in numbers_text]


def main(notes):
    rules, my_ticket, nearby_tickets = extract(notes)
    ranges = extract_range(rules)
    my_ticket = extract_numbers(my_ticket)
    nearby_tickets = extract_numbers(nearby_tickets)

    invalid_tickets = [
        field_value
        for ticket in nearby_tickets
        for field_value in ticket
        if field_value not in ranges
    ]

    return sum(invalid_tickets)


if __name__ == "__main__":
    with open("input.txt") as f:
        notes = [note for note in f.read().splitlines(False) if note.strip() != ""]

    error_rate = main(notes)
    print(error_rate)
