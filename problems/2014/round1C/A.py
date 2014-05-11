import gcj
import fractions

class Solver(gcj.Solver):
    def _solve_one(self):
        f = self._getstringline()
        P, Q = map(int, f.split('/'))
        D = fractions.gcd(P, Q)
        P /= D
        Q /= D
        # test Q is power of 2
        q = Q
        r = 0
        while r==0 and q > 1:
            q, r = divmod(q, 2)
        if not (q==1 and r==0):
            return "impossible"
        F = 2**40/Q
        P *= F
        factor = 1
        highest_gen = 0
        r = 0
        while P > 1:
            P /= 2
            highest_gen += 1
        return 40 - highest_gen
        