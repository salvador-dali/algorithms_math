# https://www.hackerrank.com/challenges/k-candy-store
def combinationsWithRepetitions(n, r):
    from math import factorial as f
    return f(n + r - 1) / f(r) / f(n - 1)

for i in xrange(input()):
    print combinationsWithRepetitions(input(), input()) % 10**9