import sys, clingo
import clingo.application

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
        # Gets the solution from Clingo
        symbols = list(model.symbols(shown=True))
        # Sorts the solution
        symbols.sort()
        # Prints the sorted solution
        print(" ".join(str(s) for s in symbols))

clingo.application.clingo_main(ClingoApp())

