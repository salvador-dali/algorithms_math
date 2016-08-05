# https://www.hackerrank.com/challenges/sherlock-and-divisors
# check for all numbers from 1 to sqrt(n) and check if it is even.
def numberOfEvenDivisors(num):
    if num % 2:
        return 0

    divisors = 0
    for i in xrange(1, int(num**0.5) + 1):
        if num % i == 0:
            if i % 2 == 0:
                divisors += 1

            if (num / i != i and (num/i) % 2 == 0):
                divisors += 1

    return divisors

for i in xrange(input()):
    print numberOfEvenDivisors(input())