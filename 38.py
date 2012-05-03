def solve():
    biglhs = 9182
    digits = map(str, xrange(1,10))
    for lhs in xrange(9999,9183,-1):
        need = digits[:]
        for d in str(lhs):  #remove any non pandigital candidates
            if need.count(d): need.remove(d)
            else: break
        if len(need) == 5 and need == sorted(map(str, str(2*lhs))):
            biglhs = lhs
            biggest = "%s%s" % (biglhs, 2*biglhs)
            return biggest

if __name__ == '__main__':
    print solve()
