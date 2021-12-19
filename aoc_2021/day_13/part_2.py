from io import UnsupportedOperation
from typing import Dict, List, Set, Tuple


def display(points: Set[Tuple[int, ...]]) -> None:
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in points:
                print("#", end="")
            else:
                print(".", end="")
        print()


def fold(points: Set[Tuple[int, ...]], instructions: List[Dict[str, int]]) -> None:
    for instruction in instructions:
        for axis, fold_pos in instruction.items():
            if axis == "x":
                points = set(
                    (x if x < fold_pos else fold_pos - (x - fold_pos), y)
                    for x, y in points
                )
            elif axis == "y":
                points = set(
                    (x, y if y < fold_pos else fold_pos - (y - fold_pos))
                    for x, y in points
                )
            else:
                raise UnsupportedOperation(f"Unexpected axis: {axis}")

    display(points)


if __name__ == "__main__":
    with open("input.txt") as f:
        points_str, instructions_str = f.read().split("\n\n")
        points = set(
            tuple(map(int, line.split(","))) for line in points_str.splitlines(False)
        )
        instructions = []
        for instruction in instructions_str.splitlines(False):
            axis_ins, fold_pos = instruction.split("=")
            axis = axis_ins[-1]
            instructions.append({axis: int(fold_pos)})

    result = fold(points, instructions)
    print(result)
