from typing import List


def dive(instructions: List[str]) -> int:
    formatted_instructions = [instruction.split(" ") for instruction in instructions]
    x, y = 0, 0
    for direction, depth in formatted_instructions:
        depth = int(depth)
        if direction == "forward":
            x += depth
        elif direction == "up":
            y -= depth
        elif direction == "down":
            y += depth

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
