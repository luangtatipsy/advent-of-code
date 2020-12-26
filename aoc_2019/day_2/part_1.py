def main(sequence):
    idx = 0

    while idx < len(sequence):
        number = sequence[idx]

        if number == 99:
            break
        elif number == 1 or number == 2:
            idx_1, idx_2, output_idx = (
                sequence[idx + 1],
                sequence[idx + 2],
                sequence[idx + 3],
            )

            term_1, term_2 = sequence[idx_1], sequence[idx_2]
            sequence[output_idx] = term_1 + term_2 if number == 1 else term_1 * term_2

            idx += 4
            continue
        idx += 1

    return sequence[0]


if __name__ == "__main__":
    with open("input.txt") as f:
        sequence = [int(number) for number in f.read().split(",")]

    sequence[1] = 12
    sequence[2] = 2

    element = main(sequence)
    print(element)
