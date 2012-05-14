#!/bin/python
from helpers import primes, is_prime
from itertools import *


def number_familes(num):
    n = str(num)
    for i in set(n):
        if n.count(i) == 3:
            yield [int(n.replace(str(i), str(x))) for x in range(10)]


def p51():
    primelist = [p for p in primes(1000000) if p > 100001]
    for prime in primelist:
        for number_family in number_familes(prime):
            prime_family = [n for n in number_family if is_prime(n) and len(str(n)) == len(str(prime))]
            if len(prime_family) == 8 and prime in prime_family:
                print prime
                return

if __name__ == '__main__':
    p51()
