"""
https://www.hackerrank.com/challenges/the-white-lotus-and-caterpillar-game
after it is possible to find out how much steps will it take to catch caterpillar
if caterpillar is on position I and flower is on J. It will take O(1).
Therefore it is easy to get solution in O(m^2).

With a little bit of trial-error it can be decreased twice which helped to pass unit tests.

Some languages were fast enough to calculate everything with O(m^2)
"""

from math import ceil
def number(i, j, n, m):
    if abs(i - j) <= 1:
        return n - 1

    if i < j:
        return max(m - i, n - 1)

    return max(i - 1, n - 1)

def total(n, m):
    x = int(ceil((m + 1) / 2.0))
    half = 0.
    for i in xrange(1, x):
        for j in xrange(1, m + 1):
            half += number(i, j, n, m)

    half *= 2

    if m % 2 == 1:
        for j in xrange(1, m + 1):
            half += number(x, j, n, m)

    return half / m**2
    

n, m = map(int, raw_input().split())
print total(n, m)