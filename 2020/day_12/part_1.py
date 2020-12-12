from collections import deque


def move(direction, coordinate, steps):
    x, y = coordinate
    delta = {"N": -1, "W": -1, "S": 1, "E": 1}
    steps *= delta.get(direction)

    if direction == "E" or direction == "W":
        x += steps
    elif direction == "N" or direction == "S":
        y += steps

    return x, y


def rotate(directions, turn, degree):
    delta = {"R": -1, "L": 1}
    directions.rotate(delta.get(turn) * degree // 90)

    return directions


def main(nav_instructions):
    x, y = 0, 0
    directions = deque(["E", "S", "W", "N"])

    for instruction in nav_instructions:
        action, value = instruction[:1], int(instruction[1:])

        if action == "F":
            x, y = move(directions[0], coordinate=(x, y), steps=value)
        elif action == "L" or action == "R":
            rotate(directions, turn=action, degree=value)
        else:
            x, y = move(action, coordinate=(x, y), steps=value)

    return abs(x) + abs(y)


if __name__ == "__main__":
    with open("input.txt") as f:
        nav_instructions = [
            instruction.strip()
            for instruction in f.read().splitlines(False)
            if instruction.strip() != ""
        ]

    distnace = main(nav_instructions)
    print(distnace)
