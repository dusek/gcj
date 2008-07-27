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
        while True:
            # Compute value of sum for current choice of sings
            sum=0
            i=0
            factor=1
            for k in range(n-1):
                if choice[k]==0:
                    # number continues
                    continue
                else:
                    # cut and sign requested at this position
                    j=k+1 # we are offset by 1 (no sign at position 0)
                    sum+=factor*int(num[i:j])
                    if choice[k]==1:
                        factor=1
                    else:
                        factor=-1
                    i=j #next cut starts where this cut ends
            # last cut for the remainder
            sum+=factor*int(num[i:])
            # check if number is ugly
            for prime in primes:
                if sum%prime==0:
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
