import gcj

def area(x2,y2,x3,y3):
    return x3*y2-x2*y3

class Solver(gcj.Solver):
    def _solve_one(self):
        N,M,A = map(int, self._getstringline().rstrip().split(' '))
        if A>N*M:
            return "IMPOSSIBLE"
        x2=0
        y2=0
        x3=0
        y3=0
        found=False
        Xs=range(N+1)
        Ys=range(M+1)
        for x2 in Xs:
            for y2 in Ys:
                for x3 in Xs:
                    for y3 in Ys:
                        if area(x2,y2,x3,y3)==A:
                            return "%d %d %d %d %d %d" % (0, 0, x2, y2, x3, y3)
        return "IMPOSSIBLE"
