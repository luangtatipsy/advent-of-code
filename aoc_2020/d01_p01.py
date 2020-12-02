from itertools import combinations

from inputs.d1 import NUMBERS as numbers

pair_of_numbers = combinations(numbers, 2)

for x, y in pair_of_numbers:
    summation = x + y

    if summation == 2020:
        multiplication = x * y
        break

print(multiplication)
