# https://www.hackerrank.com/contests/infinitum11/challenges/confused-gorilla
def gorilla(n):
    """
    All the last points lay on the line $x + y = N$, and the probability of ending up on any
    of the point follows a binomial distribution. But it should not be calculated, because
    it is the smallest on the last points and the biggest in the center. So sorting on every
    step give a correct answer.
    :param n:
    :return:
    """
    for i in xrange(n / 2 + 1):
        print i, n - i
        if i >= n - i:
            return
        print n - i, i

for i in xrange(input()):
    gorilla(input())