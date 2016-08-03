# https://www.hackerrank.com/challenges/rectangular-game
# just noticing that the number of maximum elements in 2D array will be
# multiplication of the interception of the 2D arrays. Intersection can be found by minimum
minX, minY = 10**9, 10**9
for i in xrange(input()):
    x, y = map(int, raw_input().split(' '))
    minX, minY = min(minX, x), min(minY, y)

print minX * minY