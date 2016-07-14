# https://www.hackerrank.com/contests/infinitum12/challenges/movement-in-tree-i
# the number of visited elements is independent of the parameter H
# if one will draw a tree and mark the visited elements, it is visible that
# their number is equal to the sum of geometric progression which is
# (d^(k+1) - 1)/(d - 1) and k + 1 if d = 1
# all that is left is to calculate the the modulo of this using multiplicative inverse
def egcd(a, b):
    if a == 0:
        return b, 0, 1

    g, y, x = egcd(b % a, a)
    return g, x - b / a * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def get(d, k):
    mod = 1000000007
    if d == 1:
        return k + 1

    a = (pow(d, k + 1, mod) - 1) % mod
    b = modinv(d - 1, mod)
    return (a * b) % mod

for i in xrange(input()):
    d, k, _ = map(int, raw_input().split())
    print get(d, k)