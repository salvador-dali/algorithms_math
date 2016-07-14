# https://www.hackerrank.com/challenges/fibonacci-finding-easy
MOD = 10**9 + 7

def fibonacci(n):
    # O(log(N)) algorithm which relies on the following property
    # http://en.wikipedia.org/wiki/Fibonacci_number
    # it is derived from a matrix from removing redundant calculation
    # helper returns [F(n) and F(n + 1)]
    def helper(n):
        if n == 0:
            return 0, 1

        a, b = helper(n / 2)
        tmp = a ** 2
        c, d = 2 * a * b - tmp, b ** 2 + tmp
        return (d % MOD, (c + d) % MOD) if n % 2 else (c % MOD, d % MOD)

    return helper(n)

def fibonacci_starting(a, b, n):
    # if you start your fibonacci sequence with a, b then
    # 1a,   0b
    # 0a,   1b
    # 1a,   1b
    # 1a,   2b
    # 2a,   3b
    # 3a,   5b
    # 5a,   8b
    # and it is clear that the numbers are from the fibonacci sequence shifted by 1
    # all is needed is to calculate two previous fibonacci numbers and to multiply them by a and b
    if n == 0:
        return a

    x1, x2 = fibonacci(n - 1)
    return (x1 * a + x2 * b) % MOD

for i in xrange(input()):
    print fibonacci_starting(*map(int, raw_input().split()))