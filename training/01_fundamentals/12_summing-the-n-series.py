# https://www.hackerrank.com/challenges/summing-the-n-series
# N^2 - (N-1)^2 = 2n -1
# sum of these elements will be n^2. Using modular multiplication: you get the answer
def n_series(n):
    m = 10**9 + 7
    return ((n % m)**2) % m

for i in xrange(input()):
    print n_series(input())