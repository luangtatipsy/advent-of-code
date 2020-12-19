def extract(equation):
    return [
        char if char in "()+*" else int(char) for char in equation if char.strip() != ""
    ]


def calculate(expressions, idx):
    result = 0
    is_mul = False
    is_add = False

    while idx < len(expressions):
        expression = expressions[idx]

        if isinstance(expression, int) or expression == "(":
            if expression == "(":
                expression, idx = calculate(expressions, idx + 1)

            if is_mul:
                result *= expression
                is_mul = False
            elif is_add:
                result += expression
                is_add = False
            else:
                result = expression

        elif expression == "*":
            is_mul = True
        elif expression == "+":
            is_add = True
        elif expression == ")":
            return result, idx
        idx += 1

    return result, idx


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

    answer = main(equations)
    print(answer)
