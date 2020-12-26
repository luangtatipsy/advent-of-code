def process(sequence):
    arr = sequence[:]

    idx = 0
    while idx < len(arr):
        number = arr[idx]

        if number == 99:
            break
        elif number == 1 or number == 2:
            idx_1, idx_2, output_idx = (
                arr[idx + 1],
                arr[idx + 2],
                arr[idx + 3],
            )

            term_1, term_2 = arr[idx_1], arr[idx_2]
            arr[output_idx] = term_1 + term_2 if number == 1 else term_1 * term_2

            idx += 4
            continue

    return arr[0]


def main(sequence):
    for noun in range(100):
        for verb in range(100):
            sequence[1] = noun
            sequence[2] = verb

            output = process(sequence)

            if output == 19690720:
                return 100 * noun + verb


if __name__ == "__main__":
    with open("input.txt") as f:
        sequence = [int(number) for number in f.read().split(",")]

    result = main(sequence)
    print(result)
