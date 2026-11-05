import sys, clingo
import clingo.application
from sudoku_board import Sudoku


class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        # Load the Sudoku rules
        ctl.load("sudoku2.lp")
        # Load the input files
        for f in files:
            ctl.load(f)
        # Read from the standard input if there isn't a file given
        if not files:
            ctl.load("-")
        # Preps and solves the Sudoku puzzle
        ctl.ground([("base", [])])
        ctl.solve()
    def print_model(self, model, printer) -> None:
        # Gets the solution from Clingo and converts it into a sudoku object
        sudoku = Sudoku.from_model(model)
        # Prints the formatted Sudoku solution
        print(sudoku)

clingo.application.clingo_main(ClingoApp())