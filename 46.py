from helpers import gen_primes
set_primes = set(gen_primes(10000))
two_square = [2*a*a for a in range(100)]

for a in range(9,10000,2):
    for b in two_square:
        if a-b in set_primes: break
        if a-b < 0:
            print(a,b)
            break
            

    
