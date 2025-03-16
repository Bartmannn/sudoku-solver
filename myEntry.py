from tkinter import Entry, END


class MyEntry(Entry):

    def __init__(self, master, row, column, **kwargs):
        super().__init__(master=master, **kwargs)
        self.exist_numbers = []
        self.column = column
        self.row = row
        self.exist_row = []
        self.exist_column = []
        self.exist_field = []
        self.all_exist_numbers = []
        self.all_fit_numbers = []
        self.value_index = 0
        self.value = 0
        if super().get() != '':
            self.value = int(super().get())

    def set_numbers(self, exist_row, exist_column, exist_field):
        self.exist_row = list(set(exist_row))
        self.exist_column = list(set(exist_column))
        self.exist_field = list(set(exist_field))
        self.all_exist_numbers = list(set(self.exist_field + self.exist_row + self.exist_column))
        self.set_fit_numbers()

        if len(self.all_exist_numbers) == 0:
            print(f"Row: {self.row} | Column: {self.column} | Emptiness")
        if len(self.exist_row) == 1:
            self.write_value(self.exist_row[0])
        elif len(self.exist_column) == 1:
            self.write_value(self.exist_column[0])
        elif len(self.exist_field) == 1:
            self.write_value(self.exist_field[0])

    def set_fit_numbers(self):
        self.all_fit_numbers = [value for value in range(1, 10) if str(value) not in self.all_exist_numbers]

    def next_value(self):
        self.value_index = (self.value_index + 1) % len(self.all_fit_numbers)
        self.set_value(int(self.all_fit_numbers[self.value_index]))

    def write_value(self, value):
        super().delete(0, END)
        super().insert(0, f"{value}")

    def set_coords(self, column, row):
        self.row = row
        self.column = column

    def set_value(self, value):
        self.value = value
        self.write_value(self.value)

    def clear(self):
        self.set_value('')
