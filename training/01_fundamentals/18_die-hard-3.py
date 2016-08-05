# https://www.hackerrank.com/challenges/die-hard-3
# to fill the jar C with A and B is equivalent to solve the diophant equation Ax +By = C
# it has solutions only if c is divisible by gcd(a, b)
#
# and important thing I missed is that you have to fill one of the jugs, not the third jug
# in this case c <= max(a, b)
def gcd(a, b):
    while a:
        a, b = b % a, a

    return b

def diophant(a, b, c):
    return not (c % gcd(a, b)) and c <= max(a, b)

for i in xrange(input()):
    if diophant(*map(int, raw_input().split())):
        print 'YES'
    else:
        print 'NO'