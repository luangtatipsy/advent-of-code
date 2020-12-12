import math
from collections import deque


def move_to_waypoint(waypoint, coordinate, steps):
    wp_x, wp_y = waypoint
    x, y = coordinate

    x += wp_x * steps
    y += wp_y * steps

    return x, y


def move_waypoint(direction, waypoint, steps):
    wp_x, wp_y = waypoint
    delta = {"N": -1, "W": -1, "S": 1, "E": 1}
    steps *= delta.get(direction)

    if direction == "E" or direction == "W":
        wp_x += steps
    elif direction == "N" or direction == "S":
        wp_y += steps

    return wp_x, wp_y


# original source: https://stackoverflow.com/a/34374437
def rotate(origin, point, angle):
    angle = math.radians(angle)

    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return int(round(qx)), int(round(qy))


def main(nav_instructions):
    x, y, wp_x, wp_y = 0, 0, 10, -1

    for instruction in nav_instructions:
        action, value = instruction[:1], int(instruction[1:])

        if action == "F":
            x, y = move_to_waypoint(
                waypoint=(wp_x, wp_y), coordinate=(x, y), steps=value
            )
        elif action == "L" or action == "R":
            degree = -value if action == "L" else value

            wp_x, wp_y = rotate((0, 0), (wp_x, wp_y), degree)
        else:
            wp_x, wp_y = move_waypoint(
                direction=action, waypoint=(wp_x, wp_y), steps=value
            )

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
