# https://www.hackerrank.com/challenges/power-of-large-numbers
for i in xrange(input()):
    a, b = map(int, raw_input().split())
    print pow(a, b, 10**9 + 7)