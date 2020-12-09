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

    # print(numbers)
    return number


def find_encryption_weakness(numbers, invalid_number):
    start_idx = 0

    while True:
        contiguous_numbers = []
        found = False

        for number in numbers[start_idx:]:
            contiguous_numbers.append(number)
            _sum = sum(contiguous_numbers)

            if _sum > invalid_number:
                start_idx += 1
                break
            elif _sum == invalid_number:
                found = True
                break

        if found:
            break

    return min(contiguous_numbers) + max(contiguous_numbers)


def main(numbers, volume=25):
    invalid_number = find_invalid_number(numbers, volume=volume)
    # print(numbers)
    encryption_weakness = find_encryption_weakness(numbers, invalid_number)

    return encryption_weakness


if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = [
            int(number) for number in f.read().splitlines(False) if number.strip() != ""
        ]

    encryption_weakness = main(numbers, volume=25)
    print(encryption_weakness)
