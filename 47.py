from helpers import gen_primes
primes = list(gen_primes(500))

def factors(n):
    D = {}
    for x in range(2,n+1):
        D[x] = factorize(x)
    return D

def factorize(n):
    facs = []
    q = n
    for p in primes:
        if q==1:break
        while q!=1:
            if q%p == 0:
                facs.append(p)
                q = q // p
            else: break
    return facs

a=factors(150000)
b=[k for k in a if len(set(a[k])) == 4]
for x in range(3,len(b)):
    if b[x]==b[x-1]+1 and b[x-1]==b[x-2]+1 and b[x-2]==b[x-3]+1:
        print(b[x-3],b[x-2],b[x-1],b[x])

