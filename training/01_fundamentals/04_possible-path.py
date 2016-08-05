# https://www.hackerrank.com/challenges/possible-path/
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def path(a, b, x, y):
    return gcd(abs(a), abs(b)) == gcd(abs(x), abs(y))

for i in xrange(input()):
    if path(*map(int, raw_input().split())):
        print 'YES'
    else:
        print 'NO'