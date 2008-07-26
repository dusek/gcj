import gcj
import mpmath
import sys

mpmath.mp.dps=50

class Solver(gcj.Solver):
    expr=mpmath.mpf('3')+mpmath.sqrt(mpmath.mpf('5'))
    def _solve_one(self):
        n=self._getintline()
        result=mpmath.power(self.expr,mpmath.mpf(str(n)))
        return str(int(result % 1000))
