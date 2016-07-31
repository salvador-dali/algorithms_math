# https://www.hackerrank.com/challenges/dance-class
# after analysis of this sequence, you get something like
# 1, 1, 3, 2, 4, 4, 6, 4, 7, 7, 9, 7, 9, 9, 13, 10, 12, 12, 14, 12
# http://oeis.org/A059851
# and it is visible that this is sum a(n) = n - [n/2] + [n/3] - [n/4] + ...
# taking only % 2 you can see that it is
# 1 1 1 0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1
# 3 ones, 5 zeros, 7 ones, 9 zeros, and so on
# analysing this, one can see that the result will be one if
# the integer value of square root is odd
# the problem appears to find the square root precisely.
#
def superParityCheck(n):
    attempt = int(n**0.5)
    if attempt**2 > n:
        attempt -= 1
    if attempt & 1:
        return 'odd'
    else:
        return 'even'

for i in xrange(input()):
    print superParityCheck(input())