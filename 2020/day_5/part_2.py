NUM_ROWS = 128
NUM_COLS = 8


def decode(encoded, lower_char, n):
    positions = list(range(n))

    for character in encoded:
        middle_idx = len(positions) // 2

        if character == lower_char:
            positions = positions[:middle_idx]
        else:
            positions = positions[middle_idx:]

    return positions[0]


def extract_seat_id(boarding_pass):
    encoded_row = boarding_pass[:7]
    encoded_col = boarding_pass[7:]

    row = decode(encoded_row, lower_char="F", n=NUM_ROWS)
    column = decode(encoded_col, lower_char="L", n=NUM_COLS)

    return row * 8 + column


def main(boarding_passes):
    seat_indice = []
    my_seat_id = 0

    for boarding_pass in boarding_passes:
        seat_id = extract_seat_id(boarding_pass)
        seat_indice.append(seat_id)

    for seat_id in range(min(seat_indice), max(seat_indice)):
        if (
            seat_id + 1 in seat_indice
            and seat_id - 1 in seat_indice
            and seat_id not in seat_indice
        ):
            my_seat_id = seat_id
            break

    return my_seat_id


if __name__ == "__main__":
    with open("input.txt") as f:
        boarding_passes = [
            line.strip() for line in f.read().splitlines(False) if line.strip() != ""
        ]

    my_seat_id = main(boarding_passes)

    print(my_seat_id)

