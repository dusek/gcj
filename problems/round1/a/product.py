import gcj

class Solver(gcj.Solver):
    def solve(self):
        length=self._getintline()
        v1=map(int, self._getstringline().split(' '))
        v2=map(int, self._getstringline().split(' '))
        v1.sort()
        v2.sort()
        v2=list(reversed(v2))
        sum=0
        for i in range(len(v1)):
            sum+=v1[i]*v2[i]
        return sum
