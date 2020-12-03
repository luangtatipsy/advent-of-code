def encounter_tree_count(square_map):
    x_offset = 0
    encountered_count = 0
    length = len(square_map[0])

    for num_row in range(len(square_map)):
        encountered_count += 1 if square_map[num_row][x_offset] == '#' else 0

        x_offset += 3
        x_offset %= length #  Start over if `idx` is greater than the length of row
        
    return encountered_count


if __name__ == "__main__":
    with open('input.txt') as f:
        square_map = [row.strip() for row in f.read().splitlines(False) if row.strip() != '']

    encountered_count = encounter_tree_count(square_map)
    print(encountered_count)
