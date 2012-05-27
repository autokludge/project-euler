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

pb = [False] * 100000000
for p in primes(100000000):
    pb[p] = True

prime = primes(10000)
print "done prime gen"


def prime_p(n):
    if n > len(prime):
        return is_prime(n)
    else:
        return pb[n]


def good_pair(a, b):
    c = int(str(a) + str(b))
    d = int(str(b) + str(a))
    if not  prime_p(c) or not prime_p(d):
        return False
    return True


def get_combs():
    ip = is_prime
    prime_set = {}
    L = len(prime)
    for idx in xrange(1, L):
        p = prime[idx]
        if p == 5:
            continue
        prime_set[p] = set()
        for qi in range(idx, L):
            q = prime[qi]
            if ip(int(str(p) + str(q))) and ip(int(str(q) + str(p))):
                prime_set[p].add(q)
    return prime_set


def main():
    prime_set = get_combs()
    print "done prime set"
    for key in prime_set:
        for s_key in prime_set[key]:
            set_a = prime_set[key] & prime_set[s_key]
            if len(set_a) > 0:
                for t_key in set_a:
                    set_b = set_a & prime_set[t_key]
                    if len(set_b) > 0:
                        for q_key in set_b:
                            set_c = set_b & prime_set[q_key]
                            if len(set_c) > 0:
                                print key, s_key, t_key, q_key, set_c
                                print sum(key, s_key, t_key, q_key, set_c)


if __name__ == '__main__':
    main()
