import gcj
class Solver(gcj.Solver):
    def _solve_one(self):
        i = self._getintline()
        return str(i % 2 == 0).lower()
