def look_around(x, y, layout):
    num_occupied_seat = 0
    num_rows = len(layout)
    num_seats = len(layout[0])

    delta = [
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (-1, -1),
    ]

    for delta_x, delta_y in delta:
        _x = x + delta_x
        _y = y + delta_y

        while (_x >= 0 and _x < num_seats) and (_y >= 0 and _y < num_rows):
            if layout[_y][_x] == "L":
                break
            elif layout[_y][_x] == "#":
                num_occupied_seat += 1
                break

            _x += delta_x
            _y += delta_y

    return num_occupied_seat


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
                    if num_adj_seat >= 5:
                        seat_status = "L"

            row_status.append(seat_status)

        _seat_layout.append("".join(row_status))

    return _seat_layout


def main(seat_layout):
    state = []
    count = 0
    while True:
        if state == seat_layout:
            break
        else:
            state = seat_layout.copy()
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
