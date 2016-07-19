def factor(n):
    primes = [2, 3, 5, 7]
    for i in primes:
        while n % i == 0:
            n /= i
    if n == 1:
        return True
    return False

def analyse(a, b, k):
    if not factor(k):
        return 0

    res = 0
    for i in xrange(a, b + 1):
        if reduce(lambda x, y: x*y, map(int, list(str(i)))) == k:
            res += 1
    return res

for i in xrange(input()):
    a, b, k = map(int, raw_input().split())
    print 'Case ' + str(i + 1) + ':', analyse(a, b, k)