import gcj

class Solver(gcj.Solver):
    def _solve_one(self):
        N,M,A = self._getintsline()
        n,m=N,M
        if A>N*M:
            return "IMPOSSIBLE"
        elif A==N*M:
            return "0 0 %d 0 0 %d" % (N, M)
        switched=False
        if N<M:
            M,N=N,M
            switched=True
        y3=M
        x3=1
        y2=M-A%M
        x2=A/M+1
        if switched:
            x2,y2=y2,x2
            x3,y3=y3,x3
        return "%d %d %d %d %d %d" % (0, 0, x2, y2, x3, y3)
