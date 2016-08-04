# https://www.hackerrank.com/challenges/kevin-and-expected-value/
# precalculate the value for all the small* values in a cache. It will take O(n) where n ~ 5 * 10**6
# and then it will take constant time to find the value for all tests. For the bigger values we
# need to use approximation via the integral. It gives super good approximation:
# http://math.stackexchange.com/a/1043464/50804
from math import sqrt
def precalculation(n):
    s = 0
    h = {1: 0}
    for i in xrange(1, n):
        s += 0.5 + sqrt(0.25 + i)
        h[i + 1] = s / (i + 1)

    return h

def goodApproximation(n):
    z = (n - 1) * 0.5
    l = ((2 * n + 0.5) * sqrt(n + 0.25) - 0.5 * sqrt(0.25)) / 3 + z
    u = ((2 * n + 2.5) * sqrt(n + 1.25) - 2.5 * sqrt(1.25)) / 3 + z

    z = (l + u) / 2 / n
    return repr(z)

def calculate(arr):
    MAX = int(5.3 * 10**6)
    m = max(arr)
    m = m if m < MAX else MAX
    h = precalculation(m)
    for i in arr:
        if i <= m:
            print h[i]
        else:
            print goodApproximation(i)

arr = [input() for i in xrange(input())]
calculate(arr)