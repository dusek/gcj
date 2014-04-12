# to reproduce, please download my GCJ framework http://github.com/dusek/gcj
# and place this file as problems/2009/round1C/A.py and run
# bin/solve.sh 2009.round1C A <your input file> > <your output file>
# I had problems uploading ZIP archive of the linked repository as source code
# to GCJ
import gcj

class Solver(gcj.Solver):
    def _solve_one(self):
        row1 = self._getintline()
        assert 1 <= row1 and row1 <= 4
        square1 = []
        for i in range(4):
            square1.append(self._getintsline())
        row2 = self._getintline()
        assert 1 <= row2 and row2 <= 4
        square2 = []
        for i in range(4):
            square2.append(self._getintsline())
        candidates = set(square1[row1-1]) & set(square2[row2-1])
        if len(candidates)==1:
            return candidates.pop()
        elif len(candidates) > 1:
            return "Bad magician!"
        else:
            return "Volunteer cheated!"