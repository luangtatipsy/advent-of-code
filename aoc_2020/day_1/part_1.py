from itertools import combinations


def multiply_expense_report(numbers):
    pair_of_numbers = combinations(numbers, 2)

    for x, y in pair_of_numbers:
        summation = x + y

        if summation == 2020:
            multiplication = x * y
            break

    return multiplication

if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = [int(number) for number in f.read().splitlines(False) if number.strip() != '']

    multiplication = multiply_expense_report(numbers)
    print(multiplication)
