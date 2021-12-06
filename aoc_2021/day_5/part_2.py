from typing import List


class Cell:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.value = 0

    def __repr__(self) -> str:
        return str(self.value)

    def increase(self):
        self.value += 1


class Map:
    def __init__(self, max_x: int, max_y: int) -> None:
        self.grid = []
        for y in range(max_y + 1):
            _rows = []
            for x in range(max_x + 1):
                _rows.append(Cell(y, x))
            self.grid.append(_rows)

    def flatten(self):
        return [cell for row in self.grid for cell in row]

    def get(self, x: int, y: int) -> Cell:
        return self.grid[y][x]

    def mark_vent(self, x: int, y: int) -> None:
        self.get(x, y).increase()

    def pretty(self):
        from pprint import pprint

        pprint(self.grid)


def hydrothermal_venture(vents: List[str]):
    coordinates = []
    max_x = max_y = 0
    for vent in vents:
        x1y1, x2y2 = vent.split(" -> ")
        x1, y1 = map(int, x1y1.split(","))
        x2, y2 = map(int, x2y2.split(","))

        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2

        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2
        coordinates.append([(x1, y1), (x2, y2)])

    ocean_map = Map(max_x=max_x, max_y=max_y)

    for x1y1, x2y2 in coordinates:
        x1, y1 = x1y1
        x2, y2 = x2y2

        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2 + 1):
                ocean_map.mark_vent(x1, y)
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2 + 1):
                ocean_map.mark_vent(x, y1)
        else:
            move_x = move_y = 0
            if x1 < x2:
                move_x = 1
            elif x1 > x2:
                move_x = -1

            if y1 < y2:
                move_y = 1
            elif y1 > y2:
                move_y = -1

            _x, _y = x1, y1
            for _ in range(abs(x1 - x2) + 1):
                ocean_map.mark_vent(_x, _y)
                _x += move_x
                _y += move_y

    return len([cell.value for cell in ocean_map.flatten() if cell.value >= 2])


if __name__ == "__main__":
    with open("input.txt") as f:
        vents = [vent.strip() for vent in f.read().split("\n") if vent.strip() != ""]

    result = hydrothermal_venture(vents)
    print(result)
