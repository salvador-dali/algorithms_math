# https://www.hackerrank.com/contests/infinitum12/challenges/count-the-necklaces
# necklace problem is pretty well known, so it was not hard for me to
# google a solution: https://en.wikipedia.org/wiki/Necklace_(combinatorics)
# http://meta.math.stackexchange.com/questions/1868/list-of-generalizations-of-common-questions/13335#13335
# https://qchu.wordpress.com/2009/06/16/gila-iii-the-orbit-counting-lemma-and-baby-polya/
# https://qchu.wordpress.com/2009/06/21/gila-v-the-polya-enumeration-theorem-and-applications/
# https://qchu.wordpress.com/2009/06/24/gila-vi-the-cycle-index-polynomials-of-the-symmetric-groups/
# https://en.wikipedia.org/wiki/Necklace_(combinatorics)

def getDivisors(n):
    small, large = [], []
    for i in xrange(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            if i != n / i:
                large.append(n / i)

    return small + large[::-1]

def factorization(n):
    def helper(n):
        step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
        maxq = n ** 0.5
        d = 1
        q = n % 2 == 0 and 2 or 3
        while q <= maxq and n % q != 0:
            q = step(d)
            d += 1
        return q <= maxq and [q] + helper(n/q) or [n]

    return set(helper(n))

def eulerTotient(n):
    if n == 1:
        return 1

    res = n
    for i in factorization(n):
        res = res / i * (i - 1)
    return res

def answer(n, k):
    s = 0
    for d in getDivisors(n):
        s += eulerTotient(d) * pow(k, n/d)

    s /= n
    return s

n, k = map(int, raw_input().split())
print answer(n, k) % 1000000007