# https://www.hackerrank.com/contests/infinitum13/challenges/multiply
from collections import Counter, defaultdict

def divisorSum(d):
    res, m = 1, 1000000007
    for p, a in d.iteritems():
        tmp = (p**(a + 1) - 1) / (p - 1) % m
        res = (res * tmp) % m

    return res


def factorizeMany(start, arr):
    def sieve(n):
        prime = [True] * n
        result = [2]
        append = result.append
        sqrt_n = (int(n ** .5) + 1) | 1    # ensure it's odd
        for p in xrange(3, sqrt_n, 2):
            if prime[p]:
                append(p)
                prime[p*p::2*p] = [False] * ((n - p*p - 1) // (2*p) + 1)
        for p in xrange(sqrt_n, n, 2):
            if prime[p]:
                append(p)
        return result

    def memory(n, primes):
        factorization = [1] * (n + 1)
        for p in primes:
            for i in xrange(p*p, n + 1, p):
                factorization[i] = i / p

        return factorization

    def getFactors(number, h):
        if number == 1:
            return {}
        arr = []
        while h[number] != 1:
            arr.append(number / h[number])
            number = h[number]

        arr.append(number)
        return dict(Counter(arr))

    maximum = max(arr + [start]) + 3
    primes = sieve(maximum)
    h = memory(maximum, primes)

    startingDict, res = defaultdict(int, getFactors(start, h)), []
    for i in arr:
        f = getFactors(i, h)
        for k, v in f.iteritems():
            startingDict[k] += v
        res.append(divisorSum(startingDict))
    return res

from random import randint, seed
seed(0)
s = randint(1, 10**6)
arr = [randint(1, 10**5) for i in xrange(1000)]

from datetime import datetime
startTime = datetime.now()

arr = factorizeMany(s, arr)

print datetime.now() - startTime



