"""
DISCLAIMER: I did not know Chinese Remainder Theorem (CRT) before reading the AOC forum. then I have searched for it (https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
"""


def main(notes):
    start_time, bus_indice = notes
    start_time = int(start_time)
    bus_indice = [int(idx) if idx.isdigit() else idx for idx in bus_indice.split(",")]

    requirements = [
        {"mod": bus_id, "remainder": (bus_id - (i % bus_id)) % bus_id}
        for i, bus_id in enumerate(bus_indice)
        if bus_id != "x"
    ]
    requirements = sorted(requirements, key=lambda req: req["mod"], reverse=True)

    cumulative_sum = 0
    shift = 1

    for requirement in requirements:
        modulo, remainder = requirement["mod"], requirement["remainder"]

        while cumulative_sum % modulo != remainder:
            cumulative_sum += shift
        shift *= modulo

    return cumulative_sum


if __name__ == "__main__":
    with open("input.txt") as f:
        notes = [
            note.strip() for note in f.read().splitlines(False) if note.strip() != ""
        ]

    cumulative_sum = main(notes)
    print(cumulative_sum)
