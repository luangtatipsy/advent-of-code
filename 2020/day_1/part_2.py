from functools import reduce
from itertools import combinations
from operator import mul


def multiply_expense_report(numbers):
    sequences_of_numbers = combinations(numbers, 3)

    for sequence in sequences_of_numbers:
        summation = sum(sequence)

        if summation == 2020:
            multiplication = reduce(mul, sequence)
            break

    return multiplication

if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = [int(number) for number in f.read().splitlines(False) if number.strip() != '']

    multiplication = multiply_expense_report(numbers)
    print(multiplication)
