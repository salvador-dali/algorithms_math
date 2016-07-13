# https://www.hackerrank.com/contests/infinitum9/challenges/fibonacci-gcd
# gcd(Fa, Fb) = F(gcd(a, b))
# so after this just calculating the F of a big number

MOD = 10**9 + 7
def fib(n, c={0:1, 1:1}):
    if n not in c:
        x = n / 2
        c[n] = (fib(x-1) * fib(n-x-1) + fib(x) * fib(n - x)) % MOD
    return c[n]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_multiple(arr):
    return reduce(gcd, arr)

def gcd_fib(arr):
    GCD = gcd_multiple(arr)
    return fib(GCD - 1) % MOD