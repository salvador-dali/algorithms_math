mod = 10 ** 9


def brute(a, b, c, d, e, f, g, h, n):
    def getX(n):
        return 1 if n < 0 else x[n]

    def getY(n):
        return 1 if n < 0 else y[n]

    x, y = [], []
    for i in xrange(n + 1):
        el1 = getX(i - a) + getY(i - b) + getY(i - c) + i * pow(d, i, mod)
        el2 = getY(i - e) + getX(i - f) + getX(i - g) + i * pow(h, i, mod)
        x.append(el1 % mod)
        y.append(el2 % mod)

    return x[-1], y[-1]


for i in xrange(input()):
    a, b, c, d, e, f, g, h, n = map(int, raw_input().split())
    r1, r2 = brute(a, b, c, d, e, f, g, h, n)
    print r1, r2
