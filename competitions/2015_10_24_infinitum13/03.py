# https://www.hackerrank.com/contests/infinitum13/challenges/deletion-game
def solution(n, k):
    maximum = n * (n + 1) / 2
    minimum = -maximum + 2
    
    if k % 2 != maximum % 2:
        return False
    
    if minimum <= k <= maximum:
        return True
    
    return False

for i in xrange(input()):
    n, k = map(int, raw_input().split())
    print 'YES' if solution(n, k) else 'NO'