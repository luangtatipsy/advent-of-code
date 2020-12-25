def extract(instruction):
    operation, shift = instruction.split(" ")

    return operation.strip(), int(shift)


def main(instructions):
    accumulator = 0
    idx = 0
    executed_indice = []

    while True:
        if idx in executed_indice:
            break

        executed_indice.append(idx)

        instruction = instructions[idx]
        operation, shift = extract(instruction)

        if operation == "acc":
            accumulator += shift
            idx += 1
        elif operation == "jmp":
            idx += shift
        else:
            idx += 1

    return accumulator


if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = [
            line.strip() for line in f.read().splitlines(False) if line.strip() != ""
        ]

    accumulator = main(instructions)
    print(accumulator)
