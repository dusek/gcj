import gcj

class Solver(gcj.Solver):

    def _solve_one(self):
        num=self._getstringline()
        primes=(2,3,5,7)
        n=len(num)
        if n==1:
            if int(num)==1:
                return 0
            else:
                return 1
        choice=(len(num)-1)*[0]
        ugly=0
        ord0=ord('0')
        auto={2:[], 3:[], 5:[], 7:[]}
        for prime in primes:
            for cur in range(prime):
                delta=[]
                for input in range(10):
                    delta.append((10*cur+input)%prime)
                auto[prime].append(delta)
        ints=map(lambda x: ord(x)-ord('0'), num)
        while True:
            # Compute value of sum for current choice of sings
            sum=0
            i=0
            factor=1
            for prime in primes:
                modtotal=0
                mod=0
                autoprime=auto[prime]
                for k in range(n-1):
                    if choice[k]==0:
                        # number continues
                        mod=autoprime[mod][ints[k]]
                    else:
                        # cut and sign requested at this position
                        j=k+1 # we are offset by 1 (no sign at position 0)
                        modtotal+=factor*mod
                        mod=0
                        if choice[k]==1:
                            factor=1
                        else:
                            factor=-1
                        i=j #next cut starts where this cut ends
                # last cut for the remainder
                for i in range(i,n):
                    mod=autoprime[mod][ints[i]]
                modtotal+=factor*mod
                # check if number is ugly
                if modtotal%prime==0:
                    ugly+=1
                    break
            # Generate next variation:
            i=0
            while i<n-1 and choice[i]==2:
                choice[i]=0
                i+=1
            if i==n-1:
                # no variation after the last one
                break
            else:
                choice[i]+=1
        return str(ugly)
