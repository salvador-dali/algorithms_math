# https://www.hackerrank.com/challenges/fibonacci-finding-easy
MOD = 10**9 + 7

def fibonacci(n):
    def helper(n):
        if n == 0:
            return 0, 1

        a, b = helper(n / 2)
        tmp = a ** 2
        c, d = 2 * a * b - tmp, b ** 2 + tmp
        return (d % MOD, (c + d) % MOD) if n % 2 else (c % MOD, d % MOD)

    return helper(n)

def fibonacci_starting(a, b, n):
    if n == 0:
        return a

    x1, x2 = fibonacci(n - 1)
    return (x1 * a + x2 * b) % MOD

for i in xrange(input()):
    print fibonacci_starting(*map(int, raw_input().split()))