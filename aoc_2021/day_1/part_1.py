from typing import List


def count_increased_measurements(depths: List[int]) -> int:
    current_depth = depths[0]
    counter = 0

    for depth in depths[1:]:
        if depth > current_depth:
            counter += 1
        current_depth = depth

    return counter


if __name__ == "__main__":
    with open("input.txt") as f:
        depths = [
            int(number) for number in f.read().splitlines(False) if number.strip() != ""
        ]

    counter = count_increased_measurements(depths)
    print(counter)
