# https://www.hackerrank.com/challenges/sherlock-and-permutations
def C(n, k):
    result = 1
    for i in xrange(1, k + 1):
        result = result * (n - i + 1) / i
    return result

for i in xrange(input()):
    numZeros, numOnes = map(int, raw_input().split())
    print C(numOnes + numZeros - 1, numOnes - 1) % (10**9+7)