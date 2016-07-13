# https://www.hackerrank.com/contests/infinitum9/challenges/demidenko-computer-virus
# here is my solution which I was not able to finish:
# checking the numbers I found that they belong to the following sequences
# http://oeis.org/A001844, A001845, A001846, A001847, A001848, A001849
# with the generating function:
# (1 + x)^n / (1 - x)^-n, for which people suggested http://math.stackexchange.com/a/1067410/50804
# that sum (n choose i) (t + n - i choose n) where we sum from i=0 to n
# this I tried to calculate with binomial coefficients, but with no success. (timelimit)
#
#
# their solution
#

MOD = 10**9 + 7
def binomial(m, k):
    result = 1
    for i in range(k):
        if (m - i) % MOD == 0:
            return 0
        result = result * (m - i) / (i + 1)
    return result

def myAttempt(n, t):
    s, bin1 = 0, 1
    bin2 = binomial(n + t, n)
    for i in xrange(n + 1):
        if i > 0:
            bin1 = bin1 * (n - i + 1) / i

            if bin1 == 0:
                return s % MOD

            if bin2 == 0:
                return s % MOD

        s = (s + (bin1 * bin2) % MOD) % MOD
        bin2 = bin2 * (t - i) / (n + t - i)

    return s % MOD