# https://www.hackerrank.com/challenges/connecting-towns
for i in xrange(input()):
    raw_input()
    n = 1
    for i in map(int, raw_input().split()):
        n *= i

    print n % 1234567