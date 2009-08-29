import gcj

def primes(_from,_to):
    is_prime=range(_to+1)
    _primes=[]
    for i in range(len(is_prime)):
        is_prime[i]=True
    
    i=2
    while i*i <= _to:
        c=i
        if is_prime[c]:
            if c>=_from:
                _primes.append(c)
            c+=i
            while c<= _to:
                is_prime[c]=False
                c+=i
        i+=1
    while i <= _to:
        if is_prime[i] and i>=_from:
            _primes.append(i)
        i+=1
    return _primes

if __name__=='__main__':
    print primes(100,300)

class Solver(gcj.Solver):
    
    def _solve_one(self):
        A,B,P = self._getintsline()
        _primes=primes(P,B)
        divs={}
        for i in range(A,B+1):
            divs[i]=[]
            for prime in _primes:
                if i%prime==0:
                    divs[i].append(prime)
        a=range(B+1)
        for i in range(A,B+1):
            if 
