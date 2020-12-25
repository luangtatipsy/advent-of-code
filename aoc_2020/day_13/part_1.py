def main(notes):
    start_time, bus_indice = notes
    start_time = int(start_time)
    time = start_time
    bus_indice = [int(idx) for idx in bus_indice.split(",") if idx != "x"]

    while True:
        found = False

        for idx in bus_indice:
            departure = "D" if time % idx == 0 else "."

            if departure == "D":
                waiting_time = time - start_time
                bus_id = idx
                found = True
                break
        if found:
            break

        time += 1

    return waiting_time * idx


if __name__ == "__main__":
    with open("input.txt") as f:
        notes = [
            note.strip() for note in f.read().splitlines(False) if note.strip() != ""
        ]

    bus = main(notes)
    print(bus)
