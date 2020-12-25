def calculate(mass):
    return mass // 3 - 2


def main(masses):
    sum_fuel = 0

    for mass in masses:
        total = 0

        while mass > 0:
            fuel = calculate(mass)
            if fuel >= 0:
                total += fuel
            mass = fuel

        sum_fuel += total

    return sum_fuel


if __name__ == "__main__":
    with open("input.txt") as f:
        masses = [int(mass) for mass in f.read().splitlines(False)]

    requirement = main(masses)
    print(requirement)
