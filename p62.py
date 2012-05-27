from itertools import ifilter


def p62(n):
    cubes = [a ** 3 for a in range(10, 10000)]
    sorted_cube = ["".join(sorted(str(cube))) for cube in cubes]

    for dig in range(len(sorted_cube[len(sorted_cube)-1]), 0, -1):
        li = list(ifilter(lambda x: len(x) == dig, sorted_cube))
        for i in range(len(li)):
            if li.count(li[i]) == n:
                return list(ifilter(lambda x: len(str(x)) == dig, cubes))[i]


if __name__ == '__main__':
    print p62(3)
    print p62(5)
