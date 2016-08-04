# https://www.hackerrank.com/challenges/random-number-generator

from fractions import Fraction

def uniform(a, b, c):
    a, b = min(a, b), max(a, b)
    domain = 2 * a * b

    # Compute the area of the rectangle [0, A] x [0, B] within y <= C - x
    if c >= a + b:
        return '1/1'

    if c <= a:
        cover = c * c
    elif a < c <= b:
        cover = (2 * a * (c - a)) + a**2
    else:
        cover = (2 * a * (c - a)) + (2 * (a + b - c) * (c - b)) + (a + b - c)**2

    return Fraction(cover, domain)

for _ in xrange(input()):
    a, b, c = map(int, raw_input().split())
    print uniform(a, b, c)