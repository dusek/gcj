import sys

class Solver:
    def __init__(self,input):
        self.__input=input

    def _getstringline(self):
        return self.__input.readline().rstrip()

    def _getintline(self):
        return int(self._getstringline())

    def _solve_one(self):
        raise NotImplementedError("You must override the solve method")

    def solve(self):
        cases=self._getintline()
        case=0
        while cases:
            cases-=1
            case+=1
            sys.stderr.write("Solving case %d\n" % case)
            print "Case #%d: %s" % (case, self._solve_one())

def __my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

if __name__=='__main__':
    prefix='gcj.problems'
    round=sys.argv[1]
    problem=sys.argv[2]
    solvermodulename='.'.join((prefix, round, problem))
    classname='Solver'
    solvermodule=__my_import(solvermodulename)
    solverclass=getattr(solvermodule,classname)
    f=open(sys.argv[3],'rt')
    solver=solverclass(f)
    solver.solve()
    f.close()
