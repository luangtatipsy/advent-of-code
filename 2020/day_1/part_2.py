from functools import reduce
from itertools import combinations
from operator import mul

with open("input.txt") as f:
    numbers = [int(number) for number in f.read().splitlines(False) if number.strip() != '']

sequences_of_numbers = combinations(numbers, 3)

for sequence in sequences_of_numbers:
    summation = sum(sequence)

    if summation == 2020:
        multiplication = reduce(mul, sequence)
        break

print(multiplication)
