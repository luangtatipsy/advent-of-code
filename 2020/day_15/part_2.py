from collections import defaultdict, deque


def main(numbers, num_turn=30000000):
    memory = defaultdict(lambda: deque([], maxlen=2))

    for turn, number in enumerate(numbers, 1):
        memory[number].append(turn)

    last_number = number

    for turn in range(turn + 1, num_turn + 1):
        last_turn = memory[last_number]
        if len(last_turn) == 1:
            last_number = 0
        else:
            last_number = last_turn[1] - last_turn[0]
        memory[last_number].append(turn)

    return last_number


if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = [
            int(number) for number in f.read().split(",") if number.strip() != ""
        ]

    number = main(numbers)
    print(number)
