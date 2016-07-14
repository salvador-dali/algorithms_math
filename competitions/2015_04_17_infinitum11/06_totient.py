# https://www.hackerrank.com/contests/infinitum11/challenges/totient-until-the-end
# calculate how many times one can take recursive totient, till it will be equal to 1
# have not solved during the competition, but was very close
#
# here is the idea.
# to get the totient, you do not need to know the number, only it's decomposition into primes.
# for every prime, its power either increase by some amount or decrease, but important observation
# is that there is always 2^n there (surely because prime - 1 is always divisible by 2).
# so the last element to disappear will be two.
#
# Once someone would know how many two's there will be - it is basically the answer (if there were
# no divisors of 2 in the beginning, than add 1 to the answer). So how to find the number of twos.
# We need to know this for every prime number. For three it will be 1, 5 - 2, 7 will be 2 and 3 and
# because 3 is one two, it means that 7 - 2. It is an easy DP task. So we can found the number of twos
#
# another important things is to precompute the number of twos and also divisibility sieve (to quickly
# factorize numbers)

from collections import defaultdict, Counter

def sieveEratosthenes(n):
    # finds all prime numbers less then n
    # Sieve of Eratosthenes
    # http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # O(n log log n)
    # can take up to 5 * 10**8 in 21 seconds
    # http://codereview.stackexchange.com/a/42439/30711
    prime = [True] * n
    result = [2]
    append = result.append
    sqrt_n = (int(n ** .5) + 1) | 1
    for p in xrange(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            prime[p*p::p << 1] = [False] * ((n - p*p - 1) / (p << 1) + 1)

    return result + [p for p in xrange(sqrt_n, n, 2) if prime[p]]

def getDivisorSieve(n):
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
        # TODO do not store the prime number inside itself. Store -1
        if not sieve[p]:
            sieve[p] = p
        p += 2

    return sieve

def factorizationMany(numbers, sieve):
    """
    Factorize many numbers. Way faster than factorizing each number by itself
    Takes the advantage of precomputing the sieve with the largest number.
    The sieve stores information about the smallest divisor of each number.
    And then uses this information to recursively find the divisors

    if maxNumber = 4 * 10**7, it will run ~ 6 sec
    :param numbers: [99, 104, 21, 17]
    :return: [[3, 3, 11], [2, 2, 2, 13], [3, 7], [17]]
    """
    def getDivisors(sieve, num):
        divisors = []
        while num > 1:
            divisors.append(sieve[num])
            num /= sieve[num]

        return divisors

    return [getDivisors(sieve, i) for i in numbers]

def start(n1, k1, n2, k2, n3, k3, n4, k4, sieve):
    number = defaultdict(int)
    for n_, k_ in [(n1, k1), (n2, k2), (n3, k3), (n4, k4)]:
        for z in factorizationMany([n_], sieve):
            for k, v in Counter(z).iteritems():
                number[k] += v * k_

    number.pop(1, None)
    return dict(number)

def main(number, numberOfTwos):
    if not len(number):
        return 0

    total = 0 if 2 in number else 1
    for k, v in number.iteritems():
        total += numberOfTwos[k] * v
    return total


primes = sieveEratosthenes(2 * 10**6 + 1)
sieve = getDivisorSieve(2 * 10**6 + 1)
factors = factorizationMany([i - 1 for i in primes], sieve)
numberOfTwos = {2: 1}
for i in xrange(1, len(primes)):
    total = 0
    for k, v in Counter(factors[i]).iteritems():
        total += v * numberOfTwos[k]
    numberOfTwos[primes[i]] = total

for i in xrange(input()):
    n1, k1, n2, k2, n3, k3, n4, k4 = map(int, raw_input().split())
    print main(start(n1, k1, n2, k2, n3, k3, n4, k4, sieve), numberOfTwos)