# to reproduce, please download my GCJ framework http://github.com/dusek/gcj
# and place this file as problems/2009/round1C/A.py and run
# bin/solve.sh 2009.round1C A <your input file> > <your output file>
# I had problems uploading ZIP archive of the linked repository as source code
# to GCJ
import gcj
import math

class Solver(gcj.Solver):
    def _solve_one(self):
        N=self._getintline()
        R=3*[0]
        V=3*[0]
        Dims=range(len(R))
        for fly in range(N):
            line=self._getlineitems(float)
            r=line[:3]
            v=line[3:]
            for dim in Dims:
                R[dim]+=r[dim]
                V[dim]+=v[dim]
        for dim in Dims:
            R[dim]/=N
            V[dim]/=N
        if V[0]!=0 or V[1]!=0 or V[2]!=0:
            RV=0
            VV=0
            for dim in Dims:
                RV+=R[dim]*V[dim]
                VV+=V[dim]*V[dim]
            t_min=-RV/VV
            if t_min < 0:
                t_min=0
        else:
            t_min=0
        R_min=3*[0]
        for dim in Dims:
            R_min[dim]=R[dim]+t_min*V[dim]
        d_min=0
        for dim in Dims:
            d_min+=R_min[dim]*R_min[dim]
        d_min=math.sqrt(d_min)
        return "%.20f %.20f" % (d_min, t_min)
