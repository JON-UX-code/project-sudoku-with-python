import sys, clingo
import clingo.application

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        ctl.load("sudoku2.lp")

        for f in files:
            ctl.load(f)

        if not files:
            ctl.load("-")

        ctl.ground([("base", [])])
        ctl.solve()
    def print_model(self, model, printer) -> None:
        symbols = list(model.symbols(shown=True))
        symbols.sort()
        print(" ".join(str(s) for s in symbols))

clingo.application.clingo_main(ClingoApp())

