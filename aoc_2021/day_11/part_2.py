from typing import List, Optional


class DumboOctopus:
    def __init__(self, x: int, y: int, energy: int) -> None:
        self.x = x
        self.y = y
        self.energy = energy
        self.flash_count = 0

    def __repr__(self) -> str:
        return f"{self.energy}"

    def increase(self) -> None:
        self.energy += 1

    def is_flash(self) -> bool:
        return self.energy > 9

    def is_already_flashed(self) -> bool:
        return self.energy == 0

    def reset(self):
        self.energy = 0


class Ocean:
    def __init__(self, octopuses: List[List[int]]) -> None:
        self.height = len(octopuses)
        self.width = len(octopuses[0])
        self.grid = self.__create(octopuses)

    def __create(self, octopuses) -> List[List[DumboOctopus]]:
        return [
            [DumboOctopus(x, y, octopuses[y][x]) for x in range(self.width)]
            for y in range(self.height)
        ]

    def get(self, x: int, y: int) -> DumboOctopus:
        return self.grid[y][x]

    def get_adjacent(self, x: int, y: int, direction: str) -> Optional[DumboOctopus]:
        _octopus = None
        if direction == "top":
            if y - 1 >= 0:
                _octopus = self.get(x, y - 1)
        elif direction == "bottom":
            if y + 1 <= self.height - 1:
                _octopus = self.get(x, y + 1)
        elif direction == "left":
            if x - 1 >= 0:
                _octopus = self.get(x - 1, y)
        elif direction == "right":
            if x + 1 <= self.width - 1:
                _octopus = self.get(x + 1, y)
        elif direction == "top-left":
            if x - 1 >= 0 and y - 1 >= 0:
                _octopus = self.get(x - 1, y - 1)
        elif direction == "top-right":
            if x + 1 <= self.width - 1 and y - 1 >= 0:
                _octopus = self.get(x + 1, y - 1)
        elif direction == "bottom-left":
            if x - 1 >= 0 and y + 1 <= self.height - 1:
                _octopus = self.get(x - 1, y + 1)
        elif direction == "bottom-right":
            if x + 1 <= self.width - 1 and y + 1 <= self.height - 1:
                _octopus = self.get(x + 1, y + 1)

        return _octopus

    def pretty(self) -> None:
        from pprint import pprint

        pprint(self.grid)


def measure(octopuses: List[List[int]]) -> int:
    ocean = Ocean(octopuses)
    directions = [
        "top-left",
        "top",
        "top-right",
        "left",
        "right",
        "bottom-left",
        "bottom",
        "bottom-right",
    ]

    step = 0
    while True:
        step += 1

        to_check = []
        for y in range(ocean.height):
            for x in range(ocean.width):
                _octopus = ocean.get(x, y)
                _octopus.increase()
                if _octopus.is_flash():
                    to_check.append(_octopus)

        while to_check:
            _octopus = to_check.pop(0)
            if _octopus.is_already_flashed():
                continue
            _octopus.reset()

            for direction in directions:
                adj_octopus = ocean.get_adjacent(_octopus.x, _octopus.y, direction)
                if adj_octopus and not adj_octopus.is_already_flashed():
                    adj_octopus.increase()
                    if adj_octopus.is_flash():
                        to_check.append(adj_octopus)

        if all(
            ocean.get(x, y).is_already_flashed()
            for y in range(ocean.height)
            for x in range(ocean.width)
        ):
            break

    return step


if __name__ == "__main__":
    with open("input.txt") as f:
        octopuses = [
            [int(octopus) for octopus in line] for line in f.read().splitlines(False)
        ]

    result = measure(octopuses)
    print(result)
