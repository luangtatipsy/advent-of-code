def extract(equation):
    return [
        char if char in "()+*" else int(char) for char in equation if char.strip() != ""
    ]


def custom_add_multiply(expressions):
    while len(expressions) > 1:
        numbers_of_add = expressions.count("+")

        if numbers_of_add > 0:
            add_idx = expressions.index("+")
            left_exp, right_exp = expressions[add_idx - 1], expressions[add_idx + 1]
            expressions = (
                expressions[: add_idx - 1]
                + [left_exp + right_exp]
                + expressions[add_idx + 2 :]
            )
        else:
            print(expressions)
            multiply_idx = expressions.index("*")
            left_exp, right_exp = (
                expressions[multiply_idx - 1],
                expressions[multiply_idx + 1],
            )
            expressions = (
                expressions[: multiply_idx - 1]
                + [left_exp * right_exp]
                + expressions[multiply_idx + 2 :]
            )

    return expressions[0]


def calculate(expressions, idx):
    _expressions = []

    while idx < len(expressions):
        expression = expressions[idx]

        if isinstance(expression, int) or expression in "+*":
            _expressions.append(expression)
        elif expression == "(":
            expression, idx = calculate(expressions, idx + 1)
            _expressions.append(expression)
        elif expression == ")":
            return custom_add_multiply(_expressions), idx
        idx += 1

    return custom_add_multiply(_expressions), idx


def main(equations):
    total = 0

    for equation in equations:
        expressions = extract(equation)
        result = calculate(expressions, 0)
        total += result[0]

    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        equations = [equation for equation in f.read().splitlines()]

    equations = [
        "2 * 3 + (4 * 5)",
        # "5 + (8 * 3 + 9 + 3 * 4 * 3)",
        # "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
        # "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
    ]

    answer = main(equations)
    print(answer)
