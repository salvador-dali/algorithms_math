# https://www.hackerrank.com/challenges/harry-potter-and-the-floating-rocks
def gcd(a, b):
    if not a and not b:
        return 1
    while b:
        a, b = b, a % b
    return a

# translate the line to the (0, 0) location
# x1, y1 => 0, 0
# x2, y2 => x1 - x2, y2 - y1.
# Because for the number of points we do not care in which quadrant will it be,
# we can put it in the first one.
# The number of integer points between 0,0 and x, y will be gcd(x, y) - 1.
# NB that here we have to use gcd(0,0) = 1
def numOfIntPointsBetween(x1, y1, x2, y2):
    x, y = abs(x2 - x1), abs(y2 - y1)
    return gcd(x, y) - 1

for i in xrange(input()):
    print numOfIntPointsBetween(*map(int, raw_input().split()))