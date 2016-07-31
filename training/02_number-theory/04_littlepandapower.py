#https://www.hackerrank.com/challenges/littlepandapower
# the problem is just finding A^B mod X
# if B is positive - this is just pow(a, b, x)
def euclid(a, b):
    if a:
        g, y, x = euclid(b % a, a)
        return g, x - (b / a) * y, y
    else:
        return b, 0, 1

def inv(a, x):
    gcd, n, m = euclid(a, x)
    return n % x        # no need to test, numbers are coprime

def power(a, b, x):
    if b > 0:
        return pow(a, b, x)
    else:
        return pow(inv(a, x), -b, x)



for i in xrange(int(raw_input())):
    a, b, x = map(int, raw_input().split())
    print power(a, b, x)