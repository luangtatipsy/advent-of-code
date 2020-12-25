from copy import deepcopy


def extract(instruction):
    operation, shift = instruction.split(" ")

    return operation.strip(), int(shift)


def restructure(instruction_texts):
    for idx, instruction in enumerate(instruction_texts):
        operation, shift = extract(instruction)
        instruction_texts[idx] = operation, shift

    return instruction_texts


def find_operation_indice(formatted_instructions, operations=["nop", "jmp"]):
    return [
        idx
        for idx, instruction in enumerate(formatted_instructions)
        if instruction[0] in operations
    ]


def switch(operation):
    return {"nop": "jmp", "jmp": "nop"}.get(operation)


def generate(instructions, operation_indice):
    possible_instructions = []

    for o_idx in operation_indice:
        candidate = deepcopy(instructions)
        operation, shift = instructions[o_idx]

        candidate[o_idx] = (switch(operation), shift)
        possible_instructions.append(candidate)

    return possible_instructions


def main(instructions):
    instructions = restructure(instructions)
    operation_indice = find_operation_indice(instructions)
    possible_instructions = generate(instructions, operation_indice)

    for instructions_candidate in possible_instructions:
        accumulator = 0
        idx = 0
        executed_indice = []

        while True:
            if idx in executed_indice:
                break
            elif idx == len(instructions):
                return accumulator

            executed_indice.append(idx)
            operation, shift = instructions_candidate[idx]

            if operation == "acc":
                accumulator += shift
                idx += 1
            elif operation == "jmp":
                idx += shift
            else:
                idx += 1


if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = [
            line.strip() for line in f.read().splitlines(False) if line.strip() != ""
        ]

    _instructions = [
        ("nop", 0),
        ("acc", 1),
        ("jmp", 99),
    ]

    print(generate(_instructions, [0, 2]))

    accumulator = main(instructions)
    print(accumulator)
