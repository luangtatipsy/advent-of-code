def dive(instructions):
    instructions = [instruction.split(" ") for instruction in instructions]
    x, y = 0, 0
    for direction, depth in instructions:
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

    # instructions = [
    #     "forward 5",
    #     "down 5",
    #     "forward 8",
    #     "up 3",
    #     "down 8",
    #     "forward 2",
    # ]

    multiplication = dive(instructions)
    print(multiplication)
