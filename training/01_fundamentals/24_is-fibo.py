# https://www.hackerrank.com/challenges/is-fibo/
def isFib(n):
    a, b = 0, 1
    if n == a:
        return 1
    if n == b:
        return 1

    while b <= n:
        tmp = a
        a = b
        b+= tmp
        if b == n :
            return 1

    return 0


for i in xrange(int(raw_input())):
    if isFib(int(raw_input())):
        print 'IsFibo'
    else:
        print 'IsNotFibo'