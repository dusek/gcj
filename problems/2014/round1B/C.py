import gcj
import string

# Wrong solution! any DFS (on original graph) is wrong!

class Solver(gcj.Solver):
    def DFS(self, adjlist, zips, vstate, u, ziporder, badedges):
        assert vstate[u]==0
        vstate[u] = 1
        ziporder.append(zips[u])
        for v in adjlist[u]:
            if vstate[v] == 0:
                self.DFS(adjlist, zips, vstate, v, ziporder, badedges)
            elif vstate[v] == 2: # crossedge
                print "Cross edge: %d-%d" % (u, v,)
                i = adjlist[v].index(u)
                if i != 0:
                    print "Examining potential bad edges"
                    for j in range(i-1):
                        w = adjlist[v][j]
                        print "Potential bad edge %d-%d" % (v, w,)
                        if vstate[w] == 2:
                            print "Bad edge: %d-%d" % (v, w,)
                            badedges.append((v, w))
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
            badedges = []
            self.DFS(adjlist, zips, vstate, ustart, ziporder, badedges)
            if len(badedges) == 0:
                break
            for (u, v) in badedges:
                adjlist[u].remove(v)
                adjlist[v].remove(u)
        return string.join((str(zip) for zip in ziporder), '')