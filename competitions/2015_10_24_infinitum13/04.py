# https://www.hackerrank.com/contests/infinitum13/challenges/movement-in-tree-ii
mod = 1000000007

def analise(d, k, h):
    last = k - h - 1
    if last % 2 == 0:
        # d^0 + ... + d^last
        # s = sum(d**i for i in xrange(0, last + 1, 2))
        # print s % mod

        s = 1 + pow(d, 2, mod) * (pow(d, last, mod) - 1) % mod * pow(d**2 - 1, mod - 2, mod)
        print s % mod
    else:
        # d^1 + ... + d^last
        # s = sum(d**i for i in xrange(1, last + 1, 2))
        # print s % mod

        s = pow(d, 3, mod) * (pow(d, last - 1, mod) - 1) % mod * pow(d**2 - 1, mod - 2, mod) + d
        print s % mod
    return s

def get(d, k, h):
    if d == 1:
        return k + 1 if h >= k else k

    a = (pow(d, k + 1, mod) - 1) % mod
    b = pow(d - 1, mod - 2, mod)
    r = (a * b) % mod

    r -= analise(d, k, h)
    return r % mod

for i in xrange(input()):
    d, k, h = map(int, raw_input().split())
    print get(d, k, h)