# https://www.hackerrank.com/contests/infinitum13/challenges/game-with-coins
def check(a, b):
    if a == 0 or b == 0:
        return 'First'
    if (a + b) % 2:
        return 'First'
    else:
        return 'Second'

for i in xrange(input()):
    a, b = map(int, raw_input().split())
    print check(a, b)