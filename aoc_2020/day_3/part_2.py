def encounter_tree_count(square_map, right, down):
    x_offset = 0
    encountered_count = 0
    length = len(square_map[0])

    for num_row in range(0, len(square_map), down):
        encountered_count += 1 if square_map[num_row][x_offset] == '#' else 0

        x_offset += right
        x_offset %= length #  Start over if `idx` is greater than the length of row
        
    return encountered_count


def main(square_map):
    # Direction - (RIGHT, DOWN)
    STEPS = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    multiplication = 1

    for right, down in STEPS:
        multiplication *= encounter_tree_count(square_map, right, down)

    return multiplication

if __name__ == "__main__":
    with open('input.txt') as f:
        square_map = [row.strip() for row in f.read().splitlines(False) if row.strip() != '']

    multiplication = main(square_map)
    print(multiplication)
