from typing import List


class Cell:
    def __init__(self, row: int, col: int, number: int) -> None:
        self.row = row
        self.col = col
        self.number = number
        self.is_marked = False

    def __repr__(self) -> str:
        return f"{self.number}: {'T' if self.is_marked else 'F'}"

    def set_is_marked(self):
        self.is_marked = True


class Board:
    def __init__(
        self, id: int, numbers_str: str, width: int = 5, height: int = 5
    ) -> None:
        self.id = id
        self.grid = self.__create_board(numbers_str)
        self.width = width
        self.height = height
        self.is_bingo = False

    def __create_board(self, numbers_str: str):
        _grid = []

        rows = [row.strip() for row in numbers_str.split("\n") if row.strip() != ""]
        for row_no, row in enumerate(rows):
            _grid_row = []
            numbers = [int(number) for number in row.split(" ") if number.strip() != ""]

            for col_no, number in enumerate(numbers):
                _grid_row.append(Cell(row_no, col_no, int(number)))

            _grid.append(_grid_row)

        return _grid

    def get_cell(self, row: int, col: int) -> Cell:
        return self.grid[row][col]

    def get_row(self, row: int) -> List[Cell]:
        return self.grid[row]

    def get_col(self, col: int) -> List[Cell]:
        return [self.grid[row_no][col] for row_no in range(self.height)]

    def get_unmarked_cells(self) -> List[Cell]:
        unmarked_cells = []
        for row in range(self.height):
            for col in range(self.width):
                _cell = self.get_cell(row, col)
                if not _cell.is_marked:
                    unmarked_cells.append(_cell)

        return unmarked_cells

    def pretty(self):
        from pprint import pprint

        pprint(self.grid)

    def bingo(self):
        self.is_bingo = True


def __play(board: Board, number: int):
    for row_no in range(board.height):
        for col_no in range(board.width):
            cell = board.get_cell(row_no, col_no)

            if cell.number == number:
                cell.set_is_marked()


def __is_complete(board: Board) -> None:
    def __is_bingo(cells: List[Cell]):
        return all([cell.is_marked for cell in cells])

    # Start horizontal axis checking
    for row_no in range(board.height):
        row = board.get_row(row_no)
        if __is_bingo(row):
            board.bingo()
            break

    # If there is no row being bingo, do checking vertical axis
    if not board.is_bingo:
        for col_no in range(board.width):
            col = board.get_col(col_no)
            if __is_bingo(col):
                board.bingo()
                break


def play_bingo(instructions: List[str]):
    drawn_numbers_str, boards_str = instructions[0], instructions[1:]
    drawn_numbers = [int(number) for number in drawn_numbers_str.split(",")]
    boards = [
        Board(board_id, board_str) for board_id, board_str in enumerate(boards_str, 1)
    ]

    for drawn_number in drawn_numbers:
        for board in boards:
            __play(board, drawn_number)

        for board in boards:
            __is_complete(board)

            if board.is_bingo:
                if len(boards) > 1:
                    boards.remove(board)
                else:
                    unmarked_cells = board.get_unmarked_cells()
                    sum_all_unmarked = sum([cell.number for cell in unmarked_cells])

                    return sum_all_unmarked * drawn_number


if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = [
            instruction.strip()
            for instruction in f.read().split("\n\n")
            if instruction.strip() != ""
        ]

    drawn_numbers, boards_str = instructions[0], instructions[1:]

    result = play_bingo(instructions)
    print(result)
