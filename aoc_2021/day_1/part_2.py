def count_three_measurement_sliding_window(depths):
    measurements = []
    length = len(depths)

    for idx in range(length):
        if idx + 3 <= length:
            sum_window = sum(depths[idx : idx + 3])
            measurements.append(sum_window)

    current_measurement = measurements[0]
    counter = 0
    for measurement in measurements[1:]:
        if measurement > current_measurement:
            counter += 1
        current_measurement = measurement

    return counter


if __name__ == "__main__":
    with open("input.txt") as f:
        depths = [
            int(number) for number in f.read().splitlines(False) if number.strip() != ""
        ]

    counter = count_three_measurement_sliding_window(depths)
    print(counter)
