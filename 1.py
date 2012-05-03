def sumrange(n,finish):
    return sum([a for a in xrange(n,finish,n)])

def main(argv):
    print sumrange(3,1000)+sumrange(5,1000)-sumrange(15,1000)
    return 0

def target(*args):
    return main, None

if __name__ == '__main__':
    import sys
    main(sys.argv)
