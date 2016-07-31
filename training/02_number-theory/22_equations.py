# https://www.hackerrank.com/challenges/equations

# find the number of solutions
# 1/x + 1/y = 1/n!
# x*n! + y*n! - xy = 0
# xa + ya - xy + a^2 = a^2
# (x-a)(y-a) = a^2
# x = z + a
# y = a^2/z + a
# these numbers satisfy the equation.
# the number of this solution depends on how many possible ways
# to do (N!)^2 / d
# So this ends up in finding the number of divisors of (N!)^2
#
# if the number can be shown as a0^b1*a1^b1*...*an^bn
# then it has (1 + b1)*(1 + b2)*...*(1 + bn) divisors

import math
# How many times each prime factor appears in the N!
# 2 appears every 2 factors, but every 4 times it appears twice
# and every 8 times trice and so on
# so it will appear sum(n//(2**e) for e in range(1, n))
# this function just rewrites it in a O(1) space complexity
def numOfPrimeFactors(n, factor):
    s, divisor = 0, factor
    for i in xrange(1, n):
        if factor ** i > n:
            break
        s += n / divisor
        divisor *= factor
    return s

# Sieve of Eratosthenes
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve(n):
    nums = [1] * (n + 1)
    nums[:2] = [0] * 2
    nums[4::2] = [0] * int(math.ceil((n - 3) / 2.0))
    for i in range(3, int((n + 1)**.5) + 1, 2):
        if nums[i]:
            for j in range(i*i, n+1, 2*i):
                nums[j] = 0

    return [i for i, k in enumerate(nums) if k]

# get all factors of N!
def getFactorsOfFactorial(n):
    return [(i, numOfPrimeFactors(n, i)) for i in sieve(n)]

# get number of divisors of N!
def divisorsOfFactorialSquared(n):
    num = 1
    arr = getFactorsOfFactorial(n)
    for i in arr:
        num *= (2 * i[1] + 1)

    return num

print divisorsOfFactorialSquared(input()) % 1000007