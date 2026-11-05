from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
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




        return cls(sudoku)
