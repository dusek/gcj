import gcj

class Solver(gcj.Solver):
    def _solve_one(self):
        line=self._getstringline()
        a=len(line)*[1]
        first=True
        for letter in "welcome to code jam":
            sum = 0
            if first:
                first = False
                prev = 1
            else:
                prev = 0
            for pos,line_let in enumerate(line):
                if letter==line_let:
                    sum+=prev
                prev=a[pos]
                a[pos]=sum%10000
        return "%04d" % a[-1]
