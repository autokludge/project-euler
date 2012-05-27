def join(*n):
    '''concatenate intergers for a new integer'''
    a = n[0]
    for b in n[1:]:
        a = a * next(10 ** n for n in range(1000) if (b < 10 ** n)) + b
    return a


def polygonal_number(r, start, until):
    n = value = 0
    while value < until:
        value = n * ((r - 2) * n - (r - 4)) / 2
        n += 1
        if value > start:
            yield value


def p61():
    gen_names = ['octagonal', 'heptagonal', 'hexagonal', 'pentagonal', \
                            'square', 'triangle']
    generated_values = [[value for value in polygonal_number(r, 1000, 10000)] for r in range(8, 2, -1)]
    data = tuple((gen_names[ind],
                    sorted((a, b) for a, b in (divmod(value, 100)
                                            for value in values)
                            if b > 9))
                    for ind, values in enumerate(generated_values))
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
        for (f, x6) in values6 if f == x5 and a == x6)
    numbers = list(join(*values[0][i:i + 2]) for i in range(5)) + \
                        [join(values[0][-1], values[0][0])]
    return sum(numbers)

if __name__ == '__main__':
    print(p61())

