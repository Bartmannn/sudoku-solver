from timeMeasure import TimeMeasurement

class SudokuSolver:
    def __init__(self, grid) -> None:
        self.grid = grid

    def print_grid(self) -> None:
        for y in range(9):
            if y % 3 == 0 and y != 0:
                print("- - - - - - - - - - - -")

            for x in range(9):
                if x % 3 == 0 and x != 0:
                    print(" | ", end="")

                if x == 8:
                    print(self.grid[y][x])
                else:
                    print(str(self.grid[y][x]) + " ", end="")

    def find_empty_cell(self) -> tuple:  # finding first 0 in grid
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    return y, x

        return None

    def check(self, row, col, num) -> bool:
        if num in self.grid[row]:  # check if number is in row
            return False

        for number in range(9):  # check if number is in column
            if self.grid[number][col] == num:
                return False

        row = row - row % 3
        col = col - col % 3

        for y in range(row, row + 3):  # check if number is in 3x3 square
            for x in range(col, col + 3):
                if self.grid[y][x] == num:
                    return False

        return True

    def solve_grid(self) -> bool:
        empty_cell = self.find_empty_cell()  # find empty cell

        if not empty_cell:  # if not found end program, otherwise asign coordinates coordinates
            return True
        else:
            y, x = empty_cell[0], empty_cell[1]

        for num in range(1, 10):
            if self.check(y, x, num):  # if number might be correct assign it and continue
                self.grid[y][x] = num

                if self.solve_grid():
                    return True
                else:
                    self.grid[y][x] = 0  # if there is no number that could be assigned, assign 0 and go back

        return False


def main():
    def default_shape():  # hard
        return [
            [0, 0, 0, 0, 0, 0, 5, 4, 8],
            [6, 5, 0, 8, 0, 9, 0, 0, 1],
            [0, 8, 3, 2, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 6, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 7, 0, 9, 6, 0, 0, 0, 5],
            [0, 6, 0, 0, 0, 1, 0, 0, 2],
            [9, 2, 0, 0, 0, 0, 7, 8, 0],
            [8, 0, 7, 6, 0, 0, 0, 0, 0],
        ]

    grid = default_shape()

    game = SudokuSolver(grid)

    time_checker = TimeMeasurement()
    time_checker.give_information("Rozwiązywanie rozwiązania")
    time_checker.start()
    try:
        game.solve_grid()
    except Exception:
        print("Couldn't find a solution")

    game.print_grid()
    time_checker.stop()
    print(f"{time_checker.get_measurement()}")


if __name__ == "__main__":
    main()
