import poker


def one_round5(hand1, hand2):
    # evaluate the hands
    score1 = poker.eval5(hand1)
    score2 = poker.eval5(hand2)
    # display the winning hand
    hand1 = '[%s]' % ' '.join(hand1)
    hand2 = '[%s]' % ' '.join(hand2)
    if score1 < score2:
        print '%s beats %s' % (hand1, hand2)
        return True
    elif score1 == score2:
        print '%s ties %s' % (hand1, hand2)
        return False
    else:
        print '%s beats %s' % (hand2, hand1)
        return False


def main():
    with(open('poker.txt')) as hands:
        p1win = 0
        for line in hands:
            player1 = line[:14].split(" ")
            player1 = [a[:-1] + a[-1].lower() for a in player1]
            player2 = line[14:].strip().split(" ")
            player2 = [a[:-1] + a[-1].lower() for a in player2]
            if one_round5(player1, player2):
                p1win += 1
        print p1win


if __name__ == '__main__':
    main()
