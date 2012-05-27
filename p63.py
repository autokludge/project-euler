from math import floor, log


def p63():
    count = 0
    for base in range(1, 15):
        for exp in range(50):
            if len(str(base ** exp)) == exp:
                count += 1
    return count


def p63fast():
    count = 0
    for x in range(1, 10):
        count += floor(log(10) / (log(10) - log(x)))
    return count

if __name__ == '__main__':
    print p63fast()
