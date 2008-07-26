import gcj

class Solver(gcj.Solver):
    def _solve_one(self):
        line=self._getstringline()
        self.n, self.A, self.B, self.C, self.D, self.x0, self.y0, self.M=map(int,line.split(' '))
        classes=[]
        for i in range(3):
            list=[]
            for j in range(3):
                list.append(0)
            classes.append(list)
        for (X,Y) in self.points():
            i = X % 3
            j = Y % 3
            classes[i][j]+=1
        total=0
        for x1 in range(3):
            for y1 in range(3):
                for y2 in range(3):
                    for x2 in range(3):
                        for x3 in range(3):
                            for y3 in range(3):
                                if ((x1+x2+x3) % 3)==0 and ((y1+y2+y3) % 3)==0:
                                    num1=classes[x1][y1]
                                    num2=classes[x2][y2]
                                    num3=classes[x3][y3]
                                    eq12=(x1==x2 and y1==y2)
                                    eq13=(x1==x3 and y1==y3)
                                    eq23=(x2==x3 and y2==y3)
                                    if eq12 and eq13:
                                        num2-=1
                                        num3-=2
                                    else:
                                        if eq12 or eq13 or eq23:
                                            num2-=1
                                    total += num1*num2*num3
                                else:
                                    pass
        return total/6

    def points(self):
        X = self.x0
        Y = self.y0
        yield (X, Y)
        for i in range(1,self.n):
            X = (self.A * X + self.B) % self.M
            Y = (self.C * Y + self.D) % self.M
            yield (X, Y)
