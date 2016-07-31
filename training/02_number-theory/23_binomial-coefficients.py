# https://www.hackerrank.com/challenges/binomial-coefficients
def factorial_mod(n, mod):
    if mod <= n:
        return 0

    res = 1
    for i in xrange(1, n + 1):
        res = (res * i) % mod

    return res

def binomialCoefficientModuloPrime(n, k, mod):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    a, b, c = factorial_mod(n, mod), factorial_mod(k, mod), factorial_mod(n - k, mod)
    d = (b * c) % mod
    return a * pow(d, mod - 2, mod) % mod

def binomialCoefficient(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    result = 1
    for i in xrange(1, k + 1):
        result = result * (n - i + 1) / i
    return result



n, k, mod = 16, 7, 7
print binomialCoefficientModuloPrime(n, k, mod)
# for i in xrange(n):
#     a = binomialCoefficient(n, i)
#     b = binomialCoefficientModuloPrime(n, i, mod)
#     print a, a % mod


# https://en.wikipedia.org/wiki/Lucas%27_theorem
# http://www.dms.umontreal.ca/~andrew/PDF/BinCoeff.pdf
# http://stackoverflow.com/questions/13106587/binomial-coefficient-modulo-142857
# http://fishi.devtail.com/weblog/2015/06/25/computing-large-binomial-coefficients-modulo-prime-non-prime/
# http://stackoverflow.com/questions/11867162/finding-binomial-co-effecient-modulo-prime-number-interview-street-challenge
# https://comeoncodeon.wordpress.com/category/algorithm/
# https://discuss.codechef.com/questions/3869/best-known-algos-for-calculating-ncr-m
# http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3856163/
# http://math.stackexchange.com/questions/222637/binomial-coefficient-modulo-prime-power