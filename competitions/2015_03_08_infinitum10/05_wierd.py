# https://www.hackerrank.com/challenges/a-weird-function
# it was obvious that you have to cacluale the sum of euler totient for triangular numbers
# another easy thing was to spot that you have to precalculate a lot of values.
# a harder part was to spot that i and (i+1)/2 are coprime (the fact is obvious when you look at 
# it now) but it took me a while to apply it to phi(a*b) = phi(a) * phi(b)
# the hardest part was to get corner case is f5
from math import sqrt, ceil, floor

def euler_totient2(n, arr):
    res = n
    for i in set(arr):
        res = res / i * (i - 1)
    return res

def get_divisor_sieve(n):
    p, n_sqrt, sieve = 3, int(n**0.5) + 1, [0] * (n + 1)

    for i in range(2, n + 1, 2):
        sieve[i] = 2

    while p <= n_sqrt:
        for i in xrange(p, n + 1, p):
            if not sieve[i]:
                sieve[i] = p

        while p < len(sieve) and sieve[p]:
            p += 2
    while p < n + 1:
        if not sieve[p]:
            sieve[p] = p
        p += 2

    return sieve

def get_divisors_from_sieve(divisor_sieve, num):
    divisors = []
    while num > 1:
        divisors.append(divisor_sieve[num])
        num /= divisor_sieve[num]

    return divisors

def factorize_many(m):
    sieve = get_divisor_sieve(m + 1)
    return [get_divisors_from_sieve(sieve, i) for i in xrange(m + 1)]

def pre_calc():
    L, R = 1, 10**12
    values = [0]
    for i in xrange(int(floor(sqrt(2 * L))), int(ceil(sqrt(2 * R))) + 1):
        val = i * (i + 1) / 2
        if L <= val <= R:
            if i % 2 == 0:
                v1, v2 = i / 2, i + 1
            else:
                v1, v2 = (i + 1) / 2, i

            res = euler_totient2(v1, arr[v1]) * euler_totient2(v2, arr[v2])
            values.append(values[-1] + res)

    return values

def f5(L, R, vals):
    s1, s2 = int(floor(sqrt(2 * L))) - 1, int(ceil(sqrt(2 * R)))
    for i in xrange(s2, s1, -1):
        if L <= i * (i + 1) / 2 <= R:
            s2 = i
            break

    have_found = False
    for i in xrange(s1, s2 + 1):
        if L <= i * (i + 1) / 2 <= R:
            s1 = i
            have_found = True
            break
    if not have_found:
        return 0

    return vals[s2] - vals[s1 - 1]

arr = factorize_many(1414250)
vals = pre_calc()
for i in xrange(input()):
    a, b = map(int, raw_input().split())
    print f5(a, b, vals)