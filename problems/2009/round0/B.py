import gcj
import sys
import string

class Offset:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def applicable(self,map,pos):
        new_pos = self.apply(pos)
        if new_pos.i < 0 or new_pos.i >=map.dim.i or new_pos.j < 0 or new_pos.j >= map.dim.j:
            return False
        else:
            return True

    def apply(self,pos):
        return Position(pos.i+self.i, pos.j+self.j)

    @staticmethod
    def North():
        return Offset(0,-1)
    @staticmethod
    def West():
        return Offset(-1,0)
    @staticmethod
    def East():
        return Offset(1,0)
    @staticmethod
    def South():
        return Offset(0,1)

    
class Offsets:
    all=(Offset.North(),Offset.West(),Offset.East(),Offset.South())

class Position:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def offset(self,offset):
        return offset.apply(self)

    def __str__(self):
        return "(%s,%s)" % (self.i,self.j)

class Map:
    def __init__(self,dim,solver):
        self.map=[]
        self.dim=dim
        for i in xrange(dim.i):
            self.map.append(map(Cell, solver._getintsline()))

    def __getitem__(self,key):
        return self.map[key.i][key.j]

    def rows(self):
        return self.map

    def positions(self):
        offset=Position(0,0)
        while offset.i < self.dim.i:
            while offset.j < self.dim.j:
                yield offset
                offset.j+=1
            offset.i+=1
            offset.j=0

class Cell:
    def __init__(self,elevation,_from=None,to=None,label_idx=None):
        if _from is None:
            _from=[]
        self.elevation=elevation
        self._from=[]
        self.to=to
        self.label_idx=label_idx

    def analyze(self, map, pos):
        """Find lowest neighbor according to problem's rules"""
        cur_min = self.elevation
        for offset in Offsets.all:
            if offset.applicable(map,pos):
                next = map[offset.apply(pos)]
                next_elev = next.elevation
                if next_elev < cur_min:
                    cur_min = next_elev
                    self.to = next
        if self.to is not None:
            self.to._from.append(self)

    def find_sink(self):
        cur=self
        next=cur.to
        while next is not None:
            cur=next
            next=cur.to
        return cur

    def label_basin(self,label_idx):
        self.label_idx=label_idx
        for pred in self._from:
            pred.label_basin(label_idx)

class Solver(gcj.Solver):
    def _solve_one(self):
        H,W = self._getintsline()
        map = Map(Offset(H,W), self)
        label_idx=0
        for pos in map.positions():
            map[pos].analyze(map,pos)
        for pos in map.positions():
            cell = map[pos]
            if cell.label_idx is None:
                cell.find_sink().label_basin(label_idx)
                label_idx+=1
        for row in map.rows():
            print ' '.join((string.ascii_lowercase[cell.label_idx] for cell in row))

    def solve(self):
        cases=self._getintline()
        case=0
        while cases:
            cases-=1
            case+=1
            sys.stderr.write("Solving case %d\n" % case)
            print "Case #%d:" % case
            self._solve_one()
