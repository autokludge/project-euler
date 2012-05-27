from __future__ import print_function
import time
def join(*n):
    '''concatenate intergers for a new integer'''
    a = n[0]
    for b in n[1:]:
        a = a * next(10**n for n in range(1000) if (b < 10**n)) + b
    return a
assert(join(123,456)==123456)
def triangle(start,until):
    n = value = 0
    while value < until:
        value = int(n*(n+1)/2)
        n+=1
        if value > start: yield value
def square(start,until):
    n = value = int(start**0.5)-1
    while value < until:
        value = int(n*n)
        n+=1
        if value > start: yield value
def pentagonal(start,until):
    n = value = 0
    while value < until:
        value = int(n*(3*n-1)/2)
        n+=1
        if value > start: yield value
def hexagonal(start,until):
    n = value = 0
    while value < until:
        value = int(n*(2*n-1))
        n+=1
        if value > start: yield value
def heptagonal(start,until):
    n = value = 0
    while value < until:
        value = int(n*(5*n-3)/2)
        n+=1
        if value > start: yield value
def octagonal(start,until):
    n = value = 0
    while value < until:
        value = int(n*(3*n-2))
        n+=1
        if value > start: yield value
def function_name(gen):
    return str(gen).split()[1]
def euler61():
    generators = (triangle, square, pentagonal, hexagonal, heptagonal, octagonal)[::-1]
    generator_names = tuple(function_name(gen) for gen in generators)
    t0 = time.clock()
    generated_values = (list(generator(1000, 10000)) for generator in generators)
#     print('Function values counted in {t} us'.format(t=1000000*(time.clock()-t0)))
    t0 = time.clock()
    data = tuple((generator_names[ind],
                sorted((a, b) for a, b in (divmod(value, 100)
                                        for value in values)
                        if b > 9))
                for ind, values in enumerate(generated_values))
    t1 = time.clock()
#     print('function divmod values generated in {t} us'.format(t=1000000*(t1-t0)))
    values = next(((a, b, c, d, e, f), (g1, g2, g3, g4, g5, g6))
        for g1, values1 in data
        for (a, x1) in values1
        for g2, values2 in data if g2 != g1
        for (b, x2) in values2 if b == x1
        for g3, values3 in data if g3 not in (g1, g2)
        for (c, x3) in values3 if c == x2
        for g4, values4 in data if g4 not in (g1, g2, g3)
        for (d, x4) in values4 if d == x3
        for g5, values5 in data if g5 not in (g1, g2, g3, g4)
        for (e, x5) in values5 if e == x4
        for g6, values6 in data if g6 not in (g1, g2, g3, g4, g5)
        for (f, x6 ) in values6 if f == x5 and a == x6)
#     print('Path {v} found in {t2} us'.format(v=values, t2=1000000*(time.clock()-t1)))
    numbers = list(join(*values[0][i:i+2]) for i in range(len(generators)-1)) + [join(values[0][-1], values[0][0])]
#     print('As numbers {thenumbers}, sum = {s}. Final timing: {t} us'.format(thenumbers=numbers, s=sum(numbers), t=1000000 * (time.clock()-t1)))
    return sum(numbers)
if __name__ == '__main__':
    print(euler61())