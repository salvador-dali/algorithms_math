# https://www.hackerrank.com/contests/infinitum11/challenges/discrete-logarithm
def modInv(a, mod):
    # calculate the modular inverse for 1 number
    def egcd(a, b):
        # extended Eucledian algorithm
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b / a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        GCD = b
        return GCD, x, y

    g, x, y = egcd(a, mod)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % mod

def dLog(a, b, m):
    k, A, c = int(m**0.5) + 1, {}, 1
    for i in xrange(k):
        if c in A:
            return -1
        if c == b:
            return i
        A[c] = i
        c = c * a % m
    inv, c = modInv(c, m), 1
    for i in xrange(k):
        if c * b % m in A:
            return k * i+A[c * b % m]
        c = c * inv % m
    return -1

for i in xrange(input()):
    print dLog(*map(int, raw_input().split()))