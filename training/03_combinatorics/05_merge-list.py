# https://www.hackerrank.com/challenges/merge-list

def C(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    result = 1
    for i in xrange(1, k + 1):
        result = result * (n - i + 1) / i
    return result

for i in xrange(input()):
    n, k = map(int, raw_input().split())
    print C(n + k, k) % (10**9 + 7)