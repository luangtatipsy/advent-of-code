def look_around(x, y, layout):
    adjacent_seats = []

    for _y in [y - 1, y, y + 1]:
        for _x in [x - 1, x, x + 1]:
            if (_y >= 0 and _y < len(layout)) and (_x >= 0 and _x < len(layout[0])):
                adjacent_seats.append(layout[_y][_x])

    return adjacent_seats.count("#")


def sit_or_stand(seat_layout, activity):
    _seat_layout = []
    look_for = "L" if activity == "sit" else "#"

    for y, row in enumerate(seat_layout):
        row_status = []
        for x, seat in enumerate(row):
            seat_status = seat

            if seat == look_for:
                num_adj_seat = look_around(x, y, seat_layout)

                if activity == "sit":
                    if num_adj_seat == 0:
                        seat_status = "#"
                else:
                    # including current seat, so it have to be increased to 5
                    if num_adj_seat >= 5:
                        seat_status = "L"

            row_status.append(seat_status)

        _seat_layout.append("".join(row_status))

    return _seat_layout


def main(seat_layout):
    state = []

    while True:
        if state == seat_layout:
            break
        else:
            state = seat_layout
            seat_layout = sit_or_stand(seat_layout, activity="sit")
            seat_layout = sit_or_stand(seat_layout, activity="stand")

    return "\n".join(seat_layout).count("#")


if __name__ == "__main__":
    with open("input.txt") as f:
        seat_layout = [
            line.strip() for line in f.read().splitlines(False) if line.strip() != ""
        ]

    num_occupied_seat = main(seat_layout)
    print(num_occupied_seat)
