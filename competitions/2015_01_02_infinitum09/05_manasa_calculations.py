# https://www.hackerrank.com/contests/infinitum9/challenges/manasa-and-calculations/editorial
# notice that the sum of all such numbers will be GCD(A, B) * some number
# this some number will be the sum of all possible p_i^(a_i - b_i), which are not equal to 0
# for example assuming that
# p     : p1, p2, ..., pn
# a - b : d1, d2, ..., dn
# power : x1, x2, ..., xn, where x_i = p_i^d_i
# so the sum will be 1 + x1 + x2 + ... + xn + x1 * x2 + x1 * x3 + ... x1 * xn + x1 * x2 * x3 + x1 * x2 * x4 + ... +
# + x1 * x2 * xn +  ... + x1 * x2 * x3 *... * xn
# which is equal to (x1 + 1) * (x2 + 1) * (x3 + 1) * ... * (xn + 1)
# so the answer is:
# GCD(A, B) * mul(x_i + 1)
#
#
# in the authors solution the result is
# x1 * x2 * x3 * ... * xn
# where x_i =
# p_i^a_i               if a_i == b_i
# p_i^a_i + p_i^b_i     if a_i != b_i

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def calculations(primes, a, b):
    mod, GCD, arr, mul = 10**9 + 7, 1, [], 1
    for i in xrange(len(primes)):
        GCD = (GCD * pow(primes[i], min(a[i], b[i]), mod)) % mod

    for i in xrange(len(primes)):
        d = a[i] - b[i]
        if d:
            arr.append(pow(primes[i], d, mod))

    for i in arr:
        mul = (mul * (i + 1)) % mod

    if not len(arr):
        mul *= 2

    return (mul * GCD) % mod


primes = [2, 3, 5, 7]
a = [2, 1, 7, 2]
b = [2, 1, 6, 2]
print calculations(primes, a, b)

