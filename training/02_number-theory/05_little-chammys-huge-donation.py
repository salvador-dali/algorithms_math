# https://www.hackerrank.com/challenges/little-chammys-huge-donation
# idea is to pre-calculate all possible values of sum i^2 (using normal formula)
# and then look in this lookup list to check whether the value belong to

import bisect
arr = [n*(n+1)*(2*n+1)/6 for n in xrange(1, 10**2)]

def numOfChildren(num):
    n = bisect.bisect_left(arr, num) + 1
    if n*(n+1)*(2*n+1)/6 > num:
        return n - 1
    return n

for i in xrange(input()):
    print numOfChildren(input())