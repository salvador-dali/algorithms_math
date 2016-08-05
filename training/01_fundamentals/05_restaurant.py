# https://www.hackerrank.com/challenges/restaurant
def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

for i in xrange(input()):
    a, b = map(int, raw_input().split())
    print a * b / (gcd(a, b)**2)