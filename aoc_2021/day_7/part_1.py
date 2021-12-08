from typing import List


def consume_fuel(positions: List[int]) -> int:
    positions.sort()
    length = len(positions)
    median = positions[length // 2]

    return sum([abs(median - position) for position in positions])


if __name__ == "__main__":
    with open("input.txt") as f:
        positions = [
            int(position.strip())
            for position in f.read().split(",")
            if position.strip() != ""
        ]

    result = consume_fuel(positions)
    print(result)
