import time
from math import ceil, sqrt
import functools


def abs(n):
    if n >= 0:
        return n
    else:
        return -n


def profile(func):
    ''' indended as a decorator function
    to check execution time. '''

    def decorate(*args):
        ''' Concrete decorator mesuring the execution
        time of the given function or method. '''
        start = time.clock()
        result = func(*args)
        end = time.clock()
        print "...profiling of '%s': took %f seconds" % (func.__name__, end - start)
        return result, end - start
    return decorate


def is_prime(val):
    ''' Fast deterministic primality check. '''
    val = abs(val)
    if val in [2, 3, 5]:
        return True
    if val == 1 or val & 1 == 0:
        return False  # not prime if 1 or even
    # val above 5 needs to be of form 6k±1
    if val > 5 and (val % 6 not in [1, 5] or val % 5 == 0):
        return False
    for i in xrange(7, int(val ** 0.5) + 1, 2):
        p1 = 5 * i
        k = p1 + i
        p2 = k + i
        if 0 in [(val - p1) % k, (val - p2) % k]:
            return False
    return True


def primes_SoE(n):
    ''' Generate an infinite sequence of prime numbers.
    '''
    D = {}

    q = 2

    while q < n:
        if q not in D:
            # q is new prime
            # yield it and mark its first multiple that
            # isn't marked already
            D[q * q] = [q]
        else:
            # q is composite D[q] holds a list of primes that
            # divide it. now that we are here, delete D[q] but
            # mark the next multiples of its prime factors to
            # prepare for further generation
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
    return D


def SoZP7(val):
    # all prime candidates > 7 are of form 210*k+(1,res[11:209])
    residues = [1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
         89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143, 149, 151, 157, 163,
         167, 169, 173, 179, 181, 187, 191, 193, 197, 199, 209, 211]

    num = val - 1 | 1              # if val even number then subtract 1
    mod = 210
    rescnt = 48           # modulus value; number of residues
    k = num / mod
    modk = mod * k
    r = 1  # kth residue group, base num value
    while num >= modk + residues[r]:
        r += 1  # find last pc position <= num
    maxprms = k * rescnt + r - 1     # max number of prime candidates
    prms = [True] * maxprms        # set all prime candidates to True

    # hash of residues offsets to compute nonprimes positions in prms
    pos = {}
    for i in xrange(rescnt):
        pos[residues[i]] = i - 1

    # sieve to eliminate nonprimes from prms
    sqrtN = int(ceil(sqrt(val)))
    modk = r = 0
    for prm in prms:
        r += 1
        if r > rescnt:
            r = 1
            modk += mod
        if not prm:
            continue
        prime = modk + residues[r]
        if prime > sqrtN:
            break
        prmstep = prime * rescnt
        for ri in residues[1:]:
            product = prime * (modk + ri)
            # compute product position index in prms
            k, rr = divmod(product, mod)
            nonprmpos = k * rescnt + pos[rr]
            for nprm in xrange(nonprmpos, maxprms, prmstep):
                prms[nprm] = False
    # the prms array now has all the positions for primes 11..N
    primes = [2, 3, 5, 7]
    if num < 9:
        return primes[:1 + num // 2]
    if num < 11:
        return primes
    modk = r = 0
    for prime in prms:
        r += 1
        if r > rescnt:
            r = 1
            modk += mod
        if prime:
            primes.append(modk + residues[r])
    return primes


def primes(n):
    """use SoZP7 as main prime generator"""
    return SoZP7(n)


class memoized(object):
    ''' Decorator. Caches a functions return value each time it is called. If called
    later with the same arguments, the cached value is returned (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)

    def __repr__(self):
        '''Return the functions docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)
