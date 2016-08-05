# https://www.hackerrank.com/challenges/matrix-tracing
# This can be done using DP, noticing that M(n, m) = M(n - 1, m) + M(n, m - 1), but this
# will surely timeout. or by just using combinatorics

# But this will also fail. So we have to precompute the factorials and calculate C(n,k) mod prime
# efficiently

def binomialCoefficientModuloPrime(n, k, mod, factorials):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    a, b, c = factorials[n], factorials[k], factorials[n - k]
    d = (b * c) % mod
    return a * pow(d, mod - 2, mod) % mod

factorials = [0] * (2 * 10**6 + 2)
res, mod = 1, 10**9 + 7
for i in xrange(1, 2 * 10**6 + 2):
    res = (res * i) % mod
    factorials[i] = res

for i in xrange(input()):
    n, m = map(int, raw_input().split())
    print binomialCoefficientModuloPrime(m + n - 2, m - 1, mod, factorials)