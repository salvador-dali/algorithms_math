# https://www.hackerrank.com/contests/infinitum11/challenges/prime-factorization-2
def getDivisorSieve(n):
    p, n_sqrt, sieve = 3, int(n**0.5) + 1, [0] * (n + 1)

    for i in range(2, n + 1, 2):
        sieve[i] = 2

    while p <= n_sqrt:
        for i in xrange(p, n + 1, p):
            if not sieve[i]:
                sieve[i] = p

        while sieve[p]:
            p += 2

    while p < n + 1:
        if not sieve[p]:
            sieve[p] = p
        p += 2

    return sieve

def getDivisors(sieve, num):
    total = 0
    while num > 1:
        total += sieve[num]
        num /= sieve[num]

    return total

def total(numbers):
    sieve = getDivisorSieve(2 * 10**6 + 3)
    return sum(getDivisors(sieve, i) for i in numbers)

arr = [input() for i in xrange(input())]
print total(arr)