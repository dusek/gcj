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
    import optparse
    parser=optparse.OptionParser()
    parser.add_option("-c", "--psyco",
            dest="psyco", action="store_true", dest="psyco", default=False,
            help="Use psyco to speedup run")
    parser.add_option("-p", "--profile",
            dest="profile", dest="profile", default=None, metavar="PROFILE_FILE",
            help="Profile the application and store results in the specified file")
    (opts, args) = parser.parse_args()
    if opts.psyco and opts.profile:
        sys.stderr.write("You can't use both psyco and profile at the same time.\n")
        sys.exit(1)
    if opts.psyco:
        try:
            import psyco
            psyco.full()
        except ImportError:
            sys.stderr.write("Psyco is not available; we will terminate.\n")
            sys.exit(1)
    prefix='gcj.problems'
    round=args[0]
    problem=args[1]
    solvermodulename='.'.join((prefix, round, problem))
    classname='Solver'
    solvermodule=__my_import(solvermodulename)
    solverclass=getattr(solvermodule,classname)
    f=open(args[2],'rt')
    solver=solverclass(f)
    if opts.profile:
        try:
            import hotshot
        except ImportError:
            sys.stderr.write("hotshot profiler not available; we will terminate.\n")
            sys.exit(1)
        else:
            prof=hotshot.Profile(opts.profile,lineevents=1,linetimings=1)
            prof.runcall(solver.solve)
    else:
        solver.solve()
    f.close()
