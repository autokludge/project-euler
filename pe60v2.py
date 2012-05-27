""" Project Euler Problem 60
    The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
    primes and concatenating them in any order the result will always be prime.
    For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of
    these four primes, 792, represents the lowest sum for a set of four primes
    with this property.

    Find the lowest sum for a set of five primes for which any two primes
    concatenate to produce another prime.
    """
from helpers import primes, is_prime
from itertools import combinations


pairmem = {}
def good_pair(a, b):
    key_pair = (a, b)
    if key_pair in pairmem:
        return pairmem[key_pair]
    stra = str(a)
    strb = str(b)
    result = is_prime(int(stra + strb)) \
         and is_prime(int(strb + stra))
    pairmem[key_pair] = result
    return result


def get_combs():
    seed = {3: set([3]), 7: set([7]), 9: set([9]), 13: set([13]), 17: set([17]), 19: set([19]), 23: set([23]), 29: set([29]), 31: set([31]), 37: set([37])}
    print "done prime gen"
    for prime in primes(10000)[1:]:
        print seed
        for key in seed.keys():
            print key
            gprime = True
            for pr in seed[key]:
                print pr
                if not good_pair(prime, pr):
                    gprime = False
                    break
            if gprime:
                seed[key].add(prime)
            if good_pair(prime, key):
                seed.setdefault(prime, set()).add(pr)
    print seed


def main():
    print 'entered main'
    print get_combs()


if __name__ == '__main__':
    main()
