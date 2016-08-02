# https://www.hackerrank.com/challenges/sherlock-and-queries
import collections
def one():
    return 1
def arraysFast(A, B, C):
    factors = collections.defaultdict(one)
    n, m = len(A), len(B)
    for i in range(0, m):
        factors[B[i]] = factors[B[i]] * C[i] % 1000000007

    for i, factor in factors.iteritems():
        for idx in xrange(i-1, n, i):
            A[idx] = A[idx] * factor % 1000000007

    return A


raw_input()
A = list(map(int, raw_input().split()))
B = list(map(int, raw_input().split()))
C = list(map(int, raw_input().split()))
print ' '.join(map(str, arraysFast(A, B, C)))