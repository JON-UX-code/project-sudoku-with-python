from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        # Goes through the row and column
        for row in range(1,10):
            for column in range(1,10):
                # Adds each number to the string
                s += str(self.sudoku[row, column])
                # Checks the columns and adds spaces between numbers
                if column == 1:
                    s+=(" ")
                if column == 2:
                    s+=(" ")
                if column == 3:
                    s+=("  ")
                if column == 4:
                    s+=(" ")
                if column == 5:
                    s+=(" ")
                if column == 6:
                    s+=("  ")
                if column == 7:
                    s+=(" ")
                if column == 8:
                    s+=(" ")
            # Moves to the next row
            s+="\n"
            # Add an extra line after row 3 and row 6
            if row == 3:
                s+= "\n"
            if row == 6:
                s+="\n"

        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        # Gets the Sudoku solution from Clingo
        symbols = model.symbols(shown=True)
        # For loops to get row, col, value for each cell
        for s in symbols:
            row = s.arguments[0].number
            col = s.arguments[1].number
            value = s.arguments[2].number
            # Stores the value in the Sudoku board
            sudoku[row,col] = value
        return cls(sudoku)

