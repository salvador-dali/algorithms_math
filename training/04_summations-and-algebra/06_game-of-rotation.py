# https://www.hackerrank.com/challenges/game-of-rotation
# there is an array with elements and this array is
# rotated: x1, x2, ..., xn
# will be: x2, x3, ..., x1
# and so on. We want to calculate sum from 1 to n of xi * i
# and find the maximum possible such sum
def maxMean(arr):
    # the main thing is to get that the difference between a rotation
    # will be xn - sum(xi)
    #
    # so get the starting value and the sum
    # and then iterate to find the best value
    n ,start, s = len(arr), 0, 0
    for i in xrange(n):
        start += (i + 1) * arr[i]
        s += arr[i]

    maximum = start
    for i in arr:
        start += - s + i * n
        if start > maximum:
            maximum = start

    return maximum

raw_input()
arr = list(map(int, raw_input().split()))
print maxMean(arr)