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

    basins = []
    for y in range(_map.height):
        for x in range(_map.width):
            count = 0
            point = _map.get_point(x, y)
            opened_points = [point]
            closed_points = []
            while len(opened_points) > 0:
                point = opened_points[0]
                if point not in closed_points and point.height < 9:
                    count += 1
                    closed_points.append(point)
                    left_point = _map.get_adjacent_point(point.x, point.y, "left")
                    top_point = _map.get_adjacent_point(point.x, point.y, "top")
                    right_point = _map.get_adjacent_point(point.x, point.y, "right")
                    bottom_point = _map.get_adjacent_point(point.x, point.y, "bottom")
                    adjacent_points = [
                        _point
                        for _point in [
                            left_point,
                            top_point,
                            right_point,
                            bottom_point,
                        ]
                        if _point is not None
                    ]
                    opened_points += adjacent_points

                opened_points.pop(0)
            for _point in closed_points:
                _point.height = 9
            if count > 0:
                basins.append(count)
    basins.sort()

    return basins[-1] * basins[-2] * basins[-3]


if __name__ == "__main__":
    with open("input.txt") as f:
        locations = [
            signal.strip() for signal in f.read().split("\n") if signal.strip() != ""
        ]

    result = explore(locations)
    print(result)
