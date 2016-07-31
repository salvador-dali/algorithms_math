# https://www.hackerrank.com/challenges/mehta-and-his-laziness/
# just get all the possible divisors and check how many of them has even perfect square
from fractions import Fraction
def getDivisors(n):
    small, large = [], []
    for i in xrange(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            if i != n / i:
                large.append(n / i)

    return small + large[::-1]

def probOfSquareDivisor(n):
    arr = getDivisors(n)
    l = len(arr) - 1
    d = 0
    for i in xrange(l):
        s = arr[i]**0.5
        if s % 1 == 0 and s % 2 == 0:
            d += 1

    s = str(Fraction(d, l))
    return s

for i in xrange(input()):
    print probOfSquareDivisor(input())