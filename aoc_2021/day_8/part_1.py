from typing import List


def search(signals: List[str]) -> int:
    digits = [
        digit.strip()
        for signal in signals
        for digit in signal.split("|")[1].split(" ")
        if digit.strip() != ""
    ]

    return sum(1 for digit in digits if len(digit) in [2, 3, 4, 7])


if __name__ == "__main__":
    with open("input.txt") as f:
        signals = [
            signal.strip() for signal in f.read().split("\n") if signal.strip() != ""
        ]

    result = search(signals)
    print(result)
