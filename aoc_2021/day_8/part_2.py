from typing import List, Tuple


def identify(numbers: Tuple[str, ...]) -> Tuple[str, ...]:
    n1 = [number for number in numbers if len(number) == 2][0]
    n4 = [number for number in numbers if len(number) == 4][0]
    n7 = [number for number in numbers if len(number) == 3][0]
    n8 = [number for number in numbers if len(number) == 7][0]
    # 6-segments numbers
    n9 = [
        number
        for number in numbers
        if len(number) == 6 and all(segment in number for segment in n4)
    ][0]
    n0 = [
        number
        for number in numbers
        if len(number) == 6
        and all(segment in n8 for segment in number)
        and number != n9
        and all(segment in number for segment in n1)
    ][0]
    n6 = [
        number
        for number in numbers
        if len(number) == 6 and number != n9 and number != n0
    ][0]
    # 5-digits numbers
    n5 = [
        number
        for number in numbers
        if len(number) == 5 and all(segment in n6 for segment in number)
    ][0]
    n3 = [
        number
        for number in numbers
        if len(number) == 5
        and number != n5
        and all(segment in n9 for segment in number)
    ][0]
    n2 = [
        number
        for number in numbers
        if len(number) == 5 and number != n5 and number != n3
    ][0]

    return (n0, n1, n2, n3, n4, n5, n6, n7, n8, n9)


def search(signals: List[str]) -> int:
    numbers_digits = [
        [
            tuple("".join(sorted(pattern)) for pattern in line.split())
            for line in signal.split(" | ")
        ]
        for signal in signals
    ]

    output_value = 0
    for numbers, digits in numbers_digits:
        identified_numbers = identify(numbers)
        output_value += int(
            "".join(str(identified_numbers.index(digit)) for digit in digits)
        )

    return output_value


if __name__ == "__main__":
    with open("input.txt") as f:
        signals = [
            signal.strip() for signal in f.read().split("\n") if signal.strip() != ""
        ]

    result = search(signals)
    print(result)
