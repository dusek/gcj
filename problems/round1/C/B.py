import gcj

class Solver(gcj.Solver):

    def _solve_one(self):
        num=self._getstringline()
        ugly=0
        primes=(2,3,5,7)
        choice=range(len(num)-1)
        for order in range(3**len(choice)):
            res=[]
            j=order
            factor=1
            while 3*factor<=order:
                factor*=3
            for i in range(len(choice)):
                div=j/factor
                mod=j%factor
                res.append(div)
                if factor==1:
                    break
                j=mod
                factor/=3
            prefix=[]
            for i in range(len(choice)-len(res)):
                prefix.append(0)
            prefix.extend(res)
            res=prefix
            sum=0
            i=0
            factor=1
            for k in range(len(res)):
                if res[i]==0:
                    continue
                else:
                    j=k+1
                    add=factor*int(num[i:j])
                    if choice[i]==2:
                        factor=-1
                    else:
                        factor=1
                    sum+=add
                    i=j
            if len(num)==1:
                sum=int(num)
            for prime in primes:
                if sum%prime==0:
                    #print "Sum %d is ugly" % sum
                    ugly+=1
                    break
        return str(ugly)
