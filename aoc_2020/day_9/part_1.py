from itertools import combinations


def find_invalid_number(numbers, volume=25):
    preamble_numbers = numbers[:volume]
    numbers = numbers[volume:]
    number = 0

    while len(numbers) > 0:
        number = numbers.pop(0)
        status = False

        for x, y in combinations(preamble_numbers, 2):
            if x + y == number:
                status = True
                break

        if not status:
            break

        preamble_numbers = preamble_numbers[1:]
        preamble_numbers.append(number)

    return number


if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = [
            int(number) for number in f.read().splitlines(False) if number.strip() != ""
        ]

    invalid_number = find_invalid_number(numbers, volume=25)
    print(invalid_number)
