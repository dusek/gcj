# to reproduce, please download my GCJ framework http://github.com/dusek/gcj
# and place this file as problems/2013/round0/A.py and run
# bin/solve.sh 2013.round0 A <your input file> > <your output file>
# I had problems uploading ZIP archive of the linked repository as source code
# to GCJ
import gcj
import sys

class Square(object):
    X, O, EMPTY, T = 'xo.T'
    @staticmethod
    def from_char(c):
        return {
            'X': Square.X,
            'O': Square.O,
            '.': Square.EMPTY,
            'T': Square.T,
        }[c]

class Result(object):
    X, O, DRAW, UNFINISHED = range(4)
    @staticmethod
    def to_str(r):
        return {
            Result.X: "X won",
            Result.O: "O won",
            Result.DRAW: "Draw",
            Result.UNFINISHED: "Game has not completed",
        }[r]

class Solver(gcj.Solver):
    N = 4
    def _test_row(self, row):
        candidate = None
        for j in range(self.N):
            sq = row[j]
            #print "sq = %s" % (sq,)
            if sq==Square.EMPTY:
                #print "breaking on empty"
                candidate = None
                break
            if sq==Square.T:
                #print "continuing on T"
                continue
            if candidate is None:
                #print "setting candidate to %s" % (sq,)
                candidate = sq
            elif candidate!=sq:
                #print "mismatch"
                candidate = None
                break
            else:
                pass
                #print "match"
        if candidate is not None:
            if candidate==Square.X:
                return Result.X
            elif candidate==Square.O:
                return Result.O
        
    def _solve_one(self):
        rows = []
        columns = []
        for i in range(self.N):
            columns.append([])
        diag_eqsum, diag_grow = [], []
        # read input
        empty = False
        for i in range(self.N):
            rows.append(map(Square.from_char, self._getstringline()))
            for j in range(self.N):
                square = rows[i][j]
                if square==Square.EMPTY:
                    # read remaining lines of this case and return
                    empty = True
                columns[j].append(square)
                if i==j:
                    diag_grow.append(square)
                elif i+j==self.N-1:
                    diag_eqsum.append(square)
        self._getstringline() # read empty line separating test cases
        # test rows and columns
        #print rows
        result = None
        for i in range(self.N):
            candidate = None
            row = rows[i]
            column = columns[i]
            result = self._test_row(row)
            #print "row[%d]: %s" % (i, result,)
            if result is None:
                result = self._test_row(column)
                #print "column[%d] (%s): %s" % (i, column, result,)
            if result is not None:
                break
        # test diagonals
        if result is None:
            result = self._test_row(diag_eqsum)
            #print "diag_eqsum: %s" % (result,)
            if result is None:
                result = self._test_row(diag_grow)
                #print "diag_grow: %s" % (result,)
        # return result
        if result is None:
            if empty:
                result = Result.UNFINISHED
            else:
                result = Result.DRAW
        return Result.to_str(result)
