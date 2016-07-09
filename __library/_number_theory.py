from random import randint
from collections import Counter

""" ========== GCD, LCM                     ==========

some interesting properties which might be helpful but useless to code here
gcd(n^a - 1, n^b - 1) = n^gcd(a, b) - 1
gcd(a, lcm(b, c)) = lcm(gcd(a, b), gcd(a, c))
lcm(a, gcd(b, c)) = gcd(lcm(a, b), lcm(a, c))
P|N and P|M then p = gcd(N, M)
N|P and M|p then p = lcm(N, M)
"""
def gcd(a, b):
    # calculates a greatest common divisor of two numbers
    while b:
        a, b = b, a % b
    return a

def gcd_multiple(arr):
    # calculates a greatest common multiple of array of numbers
    return reduce(gcd, arr)

def lcm(a, b):
    # calculates a least common multiple of two numbers
    return a * b / gcd(a, b)

def lcm_multiple(arr):
    # calculates a least common multiple of array of numbers
    return reduce(gcd, arr)


# ========== Primes, Divisors               ==========
def get_divisors(n):
    """Returns the list of divisors of a number in a sorted order

    O(n^0.5) To divide divisors into big and small and to remember that they come in pairs.
    So big = n / small
    """
    small, large = [], []
    for i in xrange(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            if i != n / i:
                large.append(n / i)

    return small + large[::-1]

def get_divisor_sieve(n):
    """For every number from 1 to n, find the biggest divisor for this number

    This is really helpful to factorize all the numbers really fast
    """
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
    """Knowing the divisors sieve, finds all divisors of a number

    helper to quickly factorize many numbers
    :param divisor_sieve:
    :param num:
    :return:
    """
    divisors = []
    while num > 1:
        divisors.append(divisor_sieve[num])
        num /= divisor_sieve[num]

    return divisors

def is_prime_exact(n):
    """checks whether the integer is a prime by dividing it by each odd number from 3 till sqrt(n)

    O(sqrt(n)/6)
    16 digit prime it checks in less then 2.1 seconds: 5920584932691601
    """
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def is_prime_approximate(p, n=20):
    # false positive on Carmichael number and otherwise with probability 1/2**n
    return all([pow(randint(1, p - 1), p - 1, p) == 1 for _ in xrange(n)])

def eratosthenes_sieve(n):
    """finds all prime numbers less then n

    O(n log log n) Sieve of Eratosthenes http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    can take up to 5 * 10**8 in 21 seconds http://codereview.stackexchange.com/a/42439/30711
    """
    prime, result, sqrt_n = [True] * n, [2], (int(n ** .5) + 1) | 1
    append = result.append
    for p in xrange(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            prime[p*p::p << 1] = [False] * ((n - p*p - 1) / (p << 1) + 1)

    return result + [p for p in xrange(sqrt_n, n, 2) if prime[p]]

def factorize(n):
    """factorize a number into list/set/dict of primes

    can handle arbitrary huge number, with the only thing that the maximum prime should be smaller
    then 17 digits prime: 51975335556428597. Then it will run approximately 1 minute.
    With 16 digits prime it runs approximately 5 seconds: 70804992178217648712301640058361235396058
    TODO needs nice explanation. Faster then easy method
    """
    step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
    maximum, d = n ** 0.5, 1
    q = n % 2 == 0 and 2 or 3
    while q <= maximum and n % q != 0:
        q = step(d)
        d += 1

    return [q] + factorize(n / q) if q <= maximum else [n]

def factorize_many(numbers):
    """ Factorize many numbers. Way faster than factorizing each number by itself

    Takes the advantage of precomputing the sieve with the largest number. The sieve stores
    information about the smallest divisor of each number. And then uses this information to
    recursively find the divisors. If maxNumber = 4 * 10**7, it will run ~ 6 sec

    :param numbers: [99, 104, 21, 17]
    :return: [[3, 3, 11], [2, 2, 2, 13], [3, 7], [17]]
    """
    sieve = get_divisor_sieve(max(numbers))
    return [get_divisors_from_sieve(sieve, i) for i in numbers]


# ========== Number theoretic functions     ==========
def euler_totient(n):
    """number of integers that are less then N and are coprime with it

    It is as fast as the speed of factorization, explanation and the proof
    http://en.wikipedia.org/wiki/Euler's_totient_function. Also has a nice proof using inclusion
    exclusion principle. If we need many totients, we can take advantage of factorize_many,
    and if we need totientRecursive - take a look at infinum_11 totient
    """
    res = n
    for i in set(factorize(n)):
        res = res / i * (i - 1)
    return res

def divisors_num(n):
    """Calculate the total number of divisors of the number

    important property of a divisor function
    if n = a * b and a is a coprime to b, then div(n) = div(a) * div(b)

    read also this: http://en.wikipedia.org/wiki/Divisor_function
    """
    res = 1
    for v in Counter(factorize(n)).itervalues():
        res *= v + 1
    return res

def divisor_sum(n):
    """Calculate the sum of divisors of the number

    http://en.wikipedia.org/wiki/Divisor_function
    """
    res = 1
    for p, a in Counter(factorize(n)).iteritems():
        res *= (pow(p, a + 1) - 1) / (p - 1)

    return res

def divisor_fun(n, x):
    """Calculate the divisor function of a number

    http://en.wikipedia.org/wiki/Divisor_function
    """
    res = 1
    for p, a in Counter(factorize(n)).iteritems():
        res *= (pow(p, x * (a + 1)) - 1) / (pow(p, x) - 1)

    return res

def mobius(n):
    """calculate the Mobius function of a number. It returns -1, 0, 1

    https://en.wikipedia.org/wiki/M%C3%B6bius_function
    I can use factorize method, but this one has a fast break if it finds two same divisors
    """
    factors = set([])
    def helper(n):
        step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
        maximum, d = n ** 0.5, 1
        q = n % 2 == 0 and 2 or 3
        while q <= maximum and n % q != 0:
            q = step(d)
            d += 1

        if q <= maximum:
            if q in factors:
                return -1
            else:
                factors.add(q)

            if helper(n/q) == - 1:
                return -1
        else:
            if n in factors:
                return -1
            else:
                factors.add(n)

    if n == 1:
        return 1

    if helper(n) == -1:
        return 0

    return -1 if len(factors) % 2 else 1

def mertens(n):
    """ Calculate the Mertens function  https://en.wikipedia.org/wiki/Mertens_function

    It is the sum of Mobius functions of all the numbers from 1 to n
    """
    if n == 1:
        return 1
    sieve = get_divisor_sieve(n)
    total = 1
    for i in xrange(2, n + 1):
        divisors = get_divisors_from_sieve(sieve, i)
        if len(set(divisors)) == len(divisors):
            total += -1 if len(divisors) % 2 else 1

    return total


print factorize_many([16, 253, 12345])