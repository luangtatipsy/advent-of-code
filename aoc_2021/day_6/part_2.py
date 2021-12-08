from collections import Counter
from typing import List


def grow(internal_timers: List[int]) -> int:
    # the previous solution can not solve in part, in order to solve this part, it has to be implemented with dynamic programming.
    counter = Counter(internal_timers)
    current_fishes = [
        counter[no] for no in range(9)
    ]  # 9 is the number of posible internal timers between 0 - 8

    for _ in range(256):
        # because the number of fish that its age is 0 will be reset to 6 again
        new_fishes = current_fishes[1:]
        # Append the number of fish that its age is 0 to the end of the list (create new fishes that its age is 8)
        new_fishes.append(current_fishes[0])
        # Sum the number of fish that its age is 0 and the number of fish that its age is 7 (which will be 6) together
        new_fishes[6] = current_fishes[0] + current_fishes[7]
        current_fishes = new_fishes

    return sum(current_fishes)


if __name__ == "__main__":
    with open("input.txt") as f:
        internal_timers = [
            int(internal_timer.strip())
            for internal_timer in f.read().split(",")
            if internal_timer.strip() != ""
        ]

    result = grow(internal_timers)
    print(result)
