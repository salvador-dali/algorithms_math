# https://www.hackerrank.com/contests/infinitum12/challenges/marbles
# found that the number of ways to get n marbles would be 2 time the number of ways to get n-1
# so it is easy to guess that the solution is 2^n
for i in xrange(input()):
    print pow(2, input() - 1, 1000000007)