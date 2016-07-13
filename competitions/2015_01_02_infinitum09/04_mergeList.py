# https://www.hackerrank.com/contests/infinitum9/challenges/merge-list
# this is equivalent to a combinatorial problem (n + m choose n)
from math import factorial as f
def merge(n, m):
    mod = 10**9 + 7
    return  (f(n + m) / f(n) / f(m)) % mod