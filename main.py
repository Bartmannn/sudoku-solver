"""
    Title: Sudoku solver
    Author: Bartosz Bohdziewicz
    Date: 07-08-2022 y.
"""

from tkinter import *
from myEntry import MyEntry
from tkinter import messagebox
# from timeMeasure import TimeMeasurement
from sudokuSolver import SudokuSolver

# FONT = ("Arial", 10)
# global inputs

def default_shape(): # hard
    return [
        ['', '', '', '', '', '', '5', '4', '8'],
        ['6', '5', '', '8', '', '9', '', '', '1'],
        ['', '8', '3', '2', '4', '', '', '', ''],
        ['', '', '', '', '', '', '4', '6', ''],
        ['', '', '', '1', '', '', '', '', ''],
        ['', '7', '', '9', '6', '', '', '', '5'],
        ['', '6', '', '', '', '1', '', '', '2'],
        ['9', '2', '', '', '', '', '7', '8', ''],
        ['8', '', '7', '6', '', '', '', '', ''],
    ]

def start_checking():
    time_checker = TimeMeasurement()
    time_checker.give_information("Rozwiązanie sudoku")
    time_checker.start()
    update_values()
    if solve_grid():
        messagebox.showinfo(title="Successufl", message="Sudoku has been solved.")
    else:
        messagebox.showinfo(title="Field", message="Sudoku do not have solve.")
    time_checker.stop()
    print(f"{time_checker.get_measurement()}")

def find_empty_entry():
    for y in range(9):
        for x in range(9):
            current_entry = inputs[y][x]
            if current_entry.get() == '':
                return current_entry
    return False

def get_square(coords:tuple):
    width, height = [], []
    rest_x = coords[0] % 3
    rest_y = coords[1] % 3
    if rest_x == 2:
        width = [coords[0] - 2, coords[0] - 1, coords[0]]
    elif rest_x == 1:
        width = [coords[0] - 1, coords[0], coords[0] + 1]
    else:
        width = [coords[0], coords[0] + 1, coords[0] + 2]
    if rest_y == 2:
        height = [coords[1] - 2, coords[1] - 1, coords[1]]
    elif rest_y == 1:
        height = [coords[1] - 1, coords[1], coords[1] + 1]
    else:
        height = [coords[1], coords[1] + 1, coords[1] + 2]
    coords_to_check = create_combinations(width, height)
    return [inputs[y][x].get() for x, y in coords_to_check]

def create_combinations(first_data:list, second_data:list):
    list = []
    for first_value in first_data:
        for second_value in second_data:
            list.append((first_value, second_value))
    return list

def set_properties(entry:MyEntry):
    # print(f"Row: {entry.row} | Column: {entry.column}")
    current_row = [input_value.get() for input_index, input_value in enumerate(inputs[entry.row])
                   if input_index != entry.column]
    current_column = [inputs_row[entry.column].get() for inputs_row in inputs if inputs_row != inputs[entry.row]]
    current_section = get_square((entry.column, entry.row))
    entry.set_numbers(current_row, current_column, current_section)

def get_exists_values(entry:MyEntry):
    return list(set(get_square((entry.column, entry.row)) + [input_value.get() for input_index, input_value in enumerate(inputs[entry.row])
                   if input_index != entry.column] + [inputs_row[entry.column].get() for inputs_row in inputs if inputs_row != inputs[entry.row]]))

def update_values(times=1):
    global inputs
    for _ in range(times):
        for row in range(9):
            for column in range(9):
                current_input = inputs[row][column]
                if current_input.get() == '':
                    set_properties(current_input)

def solve_grid():
    empty_entry = find_empty_entry()
    if not empty_entry:
        return True
    for fit_number in empty_entry.all_fit_numbers:
        if str(fit_number) not in get_exists_values(empty_entry):
            empty_entry.set_value(fit_number)

            if solve_grid():
                return True
            else:
                empty_entry.set_value('')

    return False

def reset():
    global inputs
    for input_row in inputs:
        for input in input_row:
            input.config(state="normal")
            input.delete(0, END)

def main():

    sudoku_solver = SudokuSolver(default_shape())
    sudoku_solver.solve_grid()

    # global inputs
    #
    # window = Tk()
    # window.title("Sudoku solver")
    #
    # title_label = Label(text="Sudoku table", font=FONT)
    # title_label.grid(row=0, column=3, columnspan=3, pady=10)
    # def_shape = default_shape()
    # inputs = [[MyEntry(window, row=y, column=x, width=3, font=FONT) for x in range(0, 9)] for y in range(9)]
    # for row_index, inputs_row in enumerate(inputs):
    #     for input_index, input in enumerate(inputs_row):
    #         if input_index in [0, 1, 2, 6, 7, 8] and row_index in [0, 1, 2, 6, 7, 8] or (input_index in [3, 4, 5] and row_index in [3, 4, 5]):
    #             input.config(bg="#DDD")
    #         ### testing ###
    #         input.insert(0, f"{def_shape[row_index][input_index]}")
    #         ###############
    #         input.grid(row=row_index+1, column=input_index, padx=5, pady=5)
    #
    # generate_button = Button(text="Check", command=start_checking)
    # generate_button.grid(row=11, column=2, columnspan=2, pady=10)
    #
    # reset_button = Button(text="Reset", command=reset)
    # reset_button.grid(row=11, column=6, columnspan=2)
    #
    # window.mainloop()

if __name__ == "__main__":
    main()
