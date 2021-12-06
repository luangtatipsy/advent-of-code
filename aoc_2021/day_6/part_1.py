from typing import List


class Lanternfish:
    def __init__(self, internal_timer: int) -> None:
        self.internal_timer = internal_timer

    def __repr__(self) -> str:
        return str(self.internal_timer)

    def live(self):
        if self.internal_timer > 0:
            self.internal_timer -= 1
        else:
            self.internal_timer = 6


def grow(internal_timers: List[int]):
    fishes = [Lanternfish(timer) for timer in internal_timers]

    for _ in range(80):
        to_be_created = 0
        for fish in fishes:
            to_be_created += int(fish.internal_timer == 0)
            fish.live()

        for _ in range(to_be_created):
            fishes.append(Lanternfish(8))

    return len(fishes)


if __name__ == "__main__":
    with open("input.txt") as f:
        internal_timers = [
            int(internal_timer.strip())
            for internal_timer in f.read().split(",")
            if internal_timer.strip() != ""
        ]

    internal_timers = [3, 4, 3, 1, 2]

    result = grow(internal_timers)
    print(result)
