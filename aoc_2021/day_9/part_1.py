from typing import List, Optional


class Point:
    def __init__(self, x: int, y: int, height: int) -> None:
        self.x = x
        self.y = y
        self.height = height

    def __repr__(self) -> str:
        return f"{self.height}"


class Map:
    def __init__(self, locations: List[str]) -> None:
        self.grid = [
            [Point(int(x), int(y), int(height)) for x, height in enumerate(row)]
            for y, row in enumerate(locations)
        ]
        self.height = len(locations)
        self.width = len(locations[0])

    def pretty(self):
        from pprint import pprint

        pprint(self.grid)

    def get_point(self, x: int, y: int) -> Point:
        return self.grid[y][x]

    def get_adjacent_point(self, x: int, y: int, direction: str) -> Optional[Point]:
        _point = None
        if direction == "top":
            if y - 1 >= 0:
                _point = self.grid[y - 1][x]
        elif direction == "bottom":
            if y + 1 <= self.height - 1:
                _point = self.grid[y + 1][x]
        elif direction == "left":
            if x - 1 >= 0:
                _point = self.grid[y][x - 1]
        elif direction == "right":
            if x + 1 <= self.width - 1:
                _point = self.grid[y][x + 1]

        return _point


def explore(locations: List[str]) -> int:
    _map = Map(locations)

    risk_points = []
    for y in range(_map.height):
        for x in range(_map.width):
            point = _map.get_point(x, y)
            left_point = _map.get_adjacent_point(x, y, "left")
            top_point = _map.get_adjacent_point(x, y, "top")
            right_point = _map.get_adjacent_point(x, y, "right")
            bottom_point = _map.get_adjacent_point(x, y, "bottom")

            if all(
                point.height < _point.height
                for _point in [
                    left_point,
                    top_point,
                    right_point,
                    bottom_point,
                ]
                if _point is not None
            ):
                risk_points.append(point)

    return sum(point.height + 1 for point in risk_points)


if __name__ == "__main__":
    with open("input.txt") as f:
        locations = [
            signal.strip() for signal in f.read().split("\n") if signal.strip() != ""
        ]

    result = explore(locations)
    print(result)
