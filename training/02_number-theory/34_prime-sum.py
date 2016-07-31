# https://www.hackerrank.com/challenges/prime-sum/
# applying Goldbach's conjecture

from random import randint
def is_prime_approximate(p, n=20):
    return all([pow(randint(1, p - 1), p - 1, p) == 1 for _ in xrange(n)])

def is_sum_of_primes(n, k):
    if n == 1:
        return False

    if n == 2 and k == 2:
        return False

    if n == 3 and k == 2:
        return False

    if k == 1:
        return is_prime_approximate(n)

    if k == 2:
        if n % 2 == 0 and n > 2:
            return True
        else:
            return is_prime_approximate(n - 2)

    if k == 3:
        return n >= 6

    return n >= 2 * k

for i in xrange(input()):
    n, k = map(int, raw_input().split())
    print 'Yes' if is_sum_of_primes(n, k) else 'No'