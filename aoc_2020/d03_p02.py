from inputs.d03 import MAP as square_map


def encounter_tree_count(square_map, right, down):
    x_offset = 0
    encountered_count = 0
    length = len(square_map[0])

    for num_row in range(0, len(square_map), down):
        encountered_count += 1 if square_map[num_row][x_offset] == '#' else 0

        x_offset += right
        x_offset %= length #  Start over if `idx` is greater than the length of row
        
    return encountered_count


# Direction - (RIGHT, DOWN)
STEPS = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]


square_map = [row.strip() for row in square_map.splitlines(False) if row.strip() != '']
multiplication = 1

for right, down in STEPS:
    multiplication *= encounter_tree_count(square_map, right, down)

print(multiplication)
