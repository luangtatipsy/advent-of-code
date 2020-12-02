from functools import reduce
from itertools import combinations
from operator import mul

from inputs.day_1 import NUMBERS as numbers

sequences_of_numbers = combinations(numbers, 3)

for sequence in sequences_of_numbers:
    summation = sum(sequence)

    if summation == 2020:
        multiplication = reduce(mul, sequence)
        break

print(multiplication)
