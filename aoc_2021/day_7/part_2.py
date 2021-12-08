from os import popen
from typing import List


def expensive_cost(n: int) -> int:
    return (n * (n + 1)) // 2


def consume_fuel(positions: List[int]) -> int:
    min_pos = min(positions)
    max_pos = max(positions)

    min_cost = float("inf")
    for n in range(min_pos, max_pos):
        cost = sum(expensive_cost(abs(n - position)) for position in positions)
        if cost < min_cost:
            min_cost = cost

    return int(min_cost)


if __name__ == "__main__":
    with open("input.txt") as f:
        positions = [
            int(position.strip())
            for position in f.read().split(",")
            if position.strip() != ""
        ]

    result = consume_fuel(positions)
    print(result)
