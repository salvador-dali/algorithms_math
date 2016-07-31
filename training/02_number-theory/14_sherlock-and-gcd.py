# https://www.hackerrank.com/challenges/sherlock-and-gcd
from fractions import gcd

for i in xrange(int(raw_input())):
    raw_input()
    if reduce(gcd, tuple(map(int, raw_input().split()))) == 1:
        print 'YES'
    else:
        print 'NO'