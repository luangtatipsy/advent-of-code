from typing import List


def dive(instructions: List[str]) -> int:
    formatted_instructions = [instruction.split(" ") for instruction in instructions]
    x, y, aim = 0, 0, 0
    for direction, depth in formatted_instructions:
        depth = int(depth)
        if direction == "forward":
            x += depth
            y += aim * depth
        elif direction == "up":
            aim -= depth
        elif direction == "down":
            aim += depth

    return x * y


if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = [
            instruction
            for instruction in f.read().splitlines(False)
            if instruction.strip() != ""
        ]

    multiplication = dive(instructions)
    print(multiplication)
