import gcj
import string

class Solver(gcj.Solver):
    def DFS(self, adjlist, zips, vstate, u, ziporder):
        assert vstate[u]==0
        vstate[u] = 1
        ziporder.append(zips[u])
        for v in adjlist[u]:
            if vstate[v] == 0:
                self.DFS(adjlist, zips, vstate, v, ziporder)
    def _solve_one(self):
        N, M = self._getintsline()
        adjlist = []
        for v in range(N):
            adjlist.append([])
        zips = []
        for v in range(N):
            zips.append(self._getintline())
        for e in range(M):
            u, v = self._getintsline()
            u -= 1
            v -= 1
            adjlist[u].append(v)
            adjlist[v].append(u)
        for adjlistu in adjlist:
            adjlistu.sort(key=lambda u: zips[u])
        vstate = N*[0] # 0 - not discovered, 1 - discovered, 2 - finished
        ustart = min(range(N), key=lambda u: zips[u])
        ziporder = []
        self.DFS(adjlist, zips, vstate, ustart, ziporder)
        return string.join((str(zip) for zip in ziporder), '')