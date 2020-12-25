import re

RE_REPLACEMENT = re.compile(r"bag[s]{0,1}")
RE_QUANTITY = re.compile(r"\d")


def extract(rule):
    outer_bag, _inner_bags = rule.split("contain")
    outer_bag = RE_REPLACEMENT.sub("", outer_bag)

    inner_bags = {}

    # `[:-1]` because of ignoring "." at the end of line
    for inner_bag in _inner_bags[:-1].split(","):
        quantity = RE_QUANTITY.findall(inner_bag)
        quantity = int(quantity[0]) if len(quantity) > 0 else 0

        inner_bag = RE_QUANTITY.sub("", inner_bag)
        inner_bag = RE_REPLACEMENT.sub("", inner_bag)

        if inner_bag.strip() != "no other":
            inner_bags[inner_bag.strip()] = quantity

    return outer_bag.strip(), inner_bags


def main(rules, my_bag="shiny gold"):
    extracted_rules = {}

    for rule in rules:
        outer_bag, inner_bags = extract(rule)
        extracted_rules[outer_bag] = inner_bags

    to_check_bags = [my_bag]
    available_bags = []

    while len(to_check_bags) > 0:
        bag = to_check_bags.pop(0)

        for outer_bag, inner_bags in extracted_rules.items():
            if bag in inner_bags:
                if outer_bag not in available_bags:
                    available_bags.append(outer_bag)
                    if outer_bag not in to_check_bags:
                        to_check_bags.append(outer_bag)

    return len(available_bags)


if __name__ == "__main__":
    with open("input.txt") as f:
        rules = [
            line.strip() for line in f.read().splitlines(False) if line.strip() != ""
        ]

    number_of_available_bags = main(rules)
    print(number_of_available_bags)
