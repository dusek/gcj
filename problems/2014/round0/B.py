# to reproduce, please download my GCJ framework http://github.com/dusek/gcj
# and place this file as problems/2009/round1C/A.py and run
# bin/solve.sh 2009.round1C A <your input file> > <your output file>
# I had problems uploading ZIP archive of the linked repository as source code
# to GCJ
import gcj
import math

class Solver(gcj.Solver):
    def _solve_one(self):
        C, F, X = self._getlineitems(float)
        n = int(math.ceil((X*F-C*F-2*C)/(C*F)))
        if n < 0:
            n = 0
        t = 0
        for i in range(n):
            t += C / (2 + i*F)
        t += X / (2 + n*F)
        return "%.7f" % t