def calculate(mass):
    return mass // 3 - 2


def main(masses):
    return sum(calculate(mass) for mass in masses)


if __name__ == "__main__":
    with open("input.txt") as f:
        masses = [int(mass) for mass in f.read().splitlines(False)]

    requirement = main(masses)
    print(requirement)
