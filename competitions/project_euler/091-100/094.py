for a in xrange(1, 50000000):
    s = 3 * a**2 - 2*a - 1.0
    # s = 3 * a**2 + 8*a + 4.0
    if s**0.5 == int(s**0.5):
        print a


# for a triangle a, a, a + 1, the square is (a+1)/4 sqrt(3*a^2-2a-1)
# a + 1, a + 1, a             a/4 sqrt(3*a^2 + 8a + 4)