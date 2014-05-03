import gcj
import string

# Wrong solution! any DFS (on original graph) is wrong!

class Solver(gcj.Solver):
    def DFS(self, adjlist, zips, vstate, u, ziporder, crossedges):
        assert vstate[u]==0
        vstate[u] = 1
        ziporder.append(zips[u])
        for v in adjlist[u]:
            if vstate[v] == 0:
                self.DFS(adjlist, zips, vstate, v, ziporder)
            elif vstate[v] == 2: # crossedge
                i = adjlist[v].find(u)
                if i != 0:
                    finished = False
                    toremove=[]
                    for j in range(i-1):
                        w = adjlist[v][i]
                        if vstate[w] == 2:
                            crossedges.append((v, w))
                            toremove.append(j)
                            adjlist[w].remove(v)
                    adjlist[v] = [adjlist[i] for i in range(len(adjlist[v])) if i not in toremove]
        vstate[u] = 2
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
        ustart = min(range(N), key=lambda u: zips[u])
        for adjlistu in adjlist:
            adjlistu.sort(key=lambda u: zips[u])
        while True:
            vstate = N*[0] # 0 - not discovered, 1 - discovered, 2 - finished
            ziporder = []
            crossedges = []
            self.DFS(adjlist, zips, vstate, ustart, ziporder, crossedges)
            if len(crossedges) == 0:
                break
        return string.join((str(zip) for zip in ziporder), '')