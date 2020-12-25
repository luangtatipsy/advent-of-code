from itertools import product


def parse_rules(rules):
    rules = [rule.strip() for rule in rules.split("\n") if rule.strip() != ""]
    rules = sorted(rules, key=lambda r: int(r[: r.index(":")]), reverse=True)
    parsed_rules = {str(i): [] for i, _ in enumerate(rules)}

    for rule in rules:
        rule_number, conditions = rule.split(":")

        if '"' in conditions:
            parsed_rule = conditions.strip().replace('"', "")
            parsed_rules[rule_number].append(parsed_rule)
        elif "|" in conditions:
            for condition in conditions.split("|"):
                _rn = condition.strip().split(" ")

                if len(_rn) > 1:
                    x, y = _rn

                    for left in parsed_rules[x]:
                        for right in parsed_rules[y]:
                            parsed_rule = "".join([left, right])
                            parsed_rules[rule_number].append(parsed_rule)
                else:
                    parsed_rule = parsed_rules[_rn[0]]
                    parsed_rules[rule_number].extend(parsed_rule)
        else:
            conditions = [parsed_rules[rn] for rn in conditions.strip().split(" ")]
            _parsed_rules = ["".join(pr) for pr in product(*conditions)]

            parsed_rules[rule_number].extend(_parsed_rules)

    return parsed_rules["0"]


def parse_messages(messages):
    return [
        message.strip()
        for message in messages.strip().split(" ")
        if message.strip() != ""
    ]


def validate(rules, messages):
    return [message for message in messages if message in rules]


if __name__ == "__main__":
    with open("input.txt") as f:
        rules, messages = f.read().split("\n\n")

    parsed_rules = parse_rules(rules)
    messages = parse_messages(messages)

    print(parsed_rules)

    valid_messages = validate(parsed_rules, messages)
    print(len(valid_messages))
