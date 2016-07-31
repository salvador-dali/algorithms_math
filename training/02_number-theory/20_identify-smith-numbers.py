# https://www.hackerrank.com/challenges/identify-smith-numbers
# trivial factorization and calculation the sum of digits in factors.
# The only important case is number 1

def factorization(n):
    def helper(n):
        step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
        maxq = n ** 0.5
        d = 1
        q = n % 2 == 0 and 2 or 3
        while q <= maxq and n % q != 0:
            q = step(d)
            d += 1
        return q <= maxq and [q] + helper(n/q) or [n]
    return helper(n)

def isSmith(n):
    if n == 1:
        return 0

    return sum(sum(map(int, str(i))) for i in factorization(n)) == sum(map(int, str(n)))


print int(isSmith(input()))