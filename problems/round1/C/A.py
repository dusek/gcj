import gcj

class Solver(gcj.Solver):
    
    def _solve_one(self):
        P,K,L = map(int, self._getstringline().split(' '))
        freqs=map(int, self._getstringline().split(' '))
        freqs.sort()
        freqs=list(reversed(freqs))
        used=len(freqs)
        i=0
        strokes=0
        if P*K<len(freqs):
            return "IMPOSSIBLE"
        position=0
        while i<used:
            position+=1
            j=i+K
            if j<used:
                strokes+=sum(freqs[i:j])*position
            else:
                strokes+=sum(freqs[i:])*position
                break
            i=j
        return str(strokes)
