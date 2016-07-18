# https://www.hackerrank.com/contests/infinitum13/challenges/integral-points/
# https://en.wikipedia.org/wiki/Shoelace_formula

def getSquare(x1, y1, x2, y2, x3, y3):
    return abs((x1 - x3) * (y2 - y1) - (x1 - x2) * (y3 - y1))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def getPointsOnSegment(x1, y1, x2, y2):
    return abs(gcd(x2 - x1, y2 - y1)) + 1

def getInsidePoints(x1, y1, x2, y2, x3, y3):
    boundary = getPointsOnSegment(x1, y1, x2, y2) + getPointsOnSegment(x2, y2, x3, y3) + getPointsOnSegment(x3, y3, x1, y1) - 3
    return (getSquare(x1, y1, x2, y2, x3, y3) - boundary + 2) / 2

for i in xrange(input()):
    x1, y1, x2, y2, x3, y3 = map(int, raw_input().split())
    print getInsidePoints(x1, y1, x2, y2, x3, y3)
