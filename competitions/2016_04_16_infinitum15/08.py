def f(x, a):
    s, x_ = 0, 1
    for i in xrange(len(a)):
        s = (s + a[i] * x_) % mod
        x_ = (x_ * x) % mod
    return s

def x_k(k, b, c, d, e):
    return (b * pow(c, 4 * k, mod) + d * pow(c, 2 * k, mod) + e) % mod

n, b, c, d, e = map(int, raw_input().split())
a = map(int, raw_input().split())
mod = 10**6 + 3
for i in xrange(n):
    print f(x_k(i, b, c, d, e), a)