from helpers import is_prime, primes, profile

def p50():
    primelist = list(primes(4000))
    for x in range(1,200):
        for y in range(x,-1,-1):
            s = sum(primelist[y:len(primelist)-(x-y)])
            if is_prime(s):
                return s

print p50()
