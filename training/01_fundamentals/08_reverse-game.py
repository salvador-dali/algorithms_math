# this is just for testing purposes to find a pattern suggests O(1) possibility
def testing(n):
    arr = range(n)
    for i in xrange(n):
        arr[i:] = reversed(arr[i:])

    print arr
    for i in enumerate(arr):
        print i

# https://www.hackerrank.com/challenges/reverse-game
def revers_game(n, k):
    if k >= n / 2:
        return 2 * (n - k - 1)
    else:
        return 2 * k + 1

for i in xrange(int(raw_input())):
    a, b = map(int, raw_input().split())
    print revers_game(a, b)
