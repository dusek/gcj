import gcj

class Solver(gcj.Solver):

    def _solve_one(self):
        n,m,X,Y,Z=self._getintsline()
        A=[]
        for i in range(m):
            A.append(self._getintline())
        sequence=list(self._sequence(A,X,Y,Z,n,m))
        return str(self._solve_work(sequence))

    def _solve_work(self,sequence):
        res=[]
        for (i,limit) in enumerate(sequence):
            smaller=1
            for j in range(i):
                if sequence[j]<limit:
                    smaller+=res[j]
            res.append(smaller)
        return sum(res)

    def _sequence(self,A,X,Y,Z,n,m):
        for i in range(n):
            yield A[i % m]
            A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z
