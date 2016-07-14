# https://www.hackerrank.com/contests/infinitum12/challenges/tricky-matrix
# I have not proved this, but I noticed that the determinant is equal to
# \frac{\displaystyle \prod_{1 \leq i <  j \leq n}(x_j - x_i) \cdot (y_j - y_i)}{\displaystyle \prod_{i=1}^{n} (x_i + y_i)}
# which is possible to calculate in O(n^2)
# and after knowing P and Q
#
# after that P/Q mod m will be (P * modinv(Q)) % m
# some relevant discussion: http://math.stackexchange.com/q/1357907/50804
#
# another relevant discussion about this matrix
# https://en.wikipedia.org/wiki/Cauchy_matrix
# http://math.stackexchange.com/q/1363012/50804


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def determinant(x, y):
    P, Q = 1, 1
    for i in x:
        for j in y:
            Q = (Q * (i + j)) % mod

    for j in xrange(len(x)):
        for i in xrange(j):
            P = (P * (x[i] - x[j]) * (y[i] - y[j])) % mod

    return (P * modinv(Q, mod)) % mod

mod = 10**9 + 7
for i in xrange(input()):
    input()
    x = list(map(int, raw_input().split()))
    y = list(map(int, raw_input().split()))
    print determinant(x, y)

