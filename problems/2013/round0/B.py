import gcj
import sys

class Solver(gcj.Solver):
    MIN_HEIGHT = 1
    MAX_HEIGHT = 100
    def _solve_one(self):
        # Excuse my brute-force...
        lawn = []
        N, M = self._getintsline()
        for i in range(N):
            row = self._getintsline()
            assert len(row)==M
            lawn.append(row)
        #print lawn
        for p in range(2**(N+M)):
            #print "p=%d" % (p,)
            test_lawn = []
            for i in range(N):
                test_lawn.append(M*[2])
            #print test_lawn
            for i in range(N+M):
                #print "i=%d" % (i,)
                if p & (1 << i):
                    # height==1
                    if i < N:
                        # i-th row
                        #print "Cutting row %d" % (i,)
                        for j in range(M):
                            n = i
                            m = j
                            if test_lawn[n][m]==2:
                                test_lawn[n][m] = 1
                    else:
                        # (i-N)-th column
                        #print "Cutting column %d" % (i-N,)
                        for j in range(N):
                            n = j
                            m = i - N
                            if test_lawn[n][m]==2:
                                test_lawn[n][m] = 1
            #print test_lawn
            if test_lawn == lawn:
                return "YES"
        return "NO"
