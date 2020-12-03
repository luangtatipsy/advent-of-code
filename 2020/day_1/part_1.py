from itertools import combinations

with open("input.txt") as f:
    numbers = [int(number) for number in f.read().splitlines(False) if number.strip() != '']

pair_of_numbers = combinations(numbers, 2)

for x, y in pair_of_numbers:
    summation = x + y

    if summation == 2020:
        multiplication = x * y
        break

print(multiplication)
