"""
https://www.hackerrank.com/challenges/ajourney
not hard to see that the number of all possible trips are 2^(n-1)

Also it is easy to see that last digits can be calculated with power modulo operations.
To calculate the first you need a lot of logs. Check library for explanation

"""
import decimal

def first(n, k):
    ln10 = decimal.Decimal(10).ln()
    ln2 = decimal.Decimal(2).ln()
    sqrt10 = decimal.Decimal(10).sqrt()
    a = ((n * ln2 / ln10 - decimal.Decimal(0.5)) % 1) * ln10
    return int(str(sqrt10 * a.exp()).replace(".", "")[0:k])

def last(n, k):
    return pow(2, n, 10**k)

def result(n, k):
    return first(n - 1, k) + last(n - 1, k)


for i in xrange(input()):
    n, k = map(int, raw_input().split())
    print result(n, k)