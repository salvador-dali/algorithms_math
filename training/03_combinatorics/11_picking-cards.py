# https://www.hackerrank.com/challenges/picking-cards
import bisect

# there are N numbers. Each number is from 0 to N
# You can select any number, that is less than the number
# of numbers you already selected
# how many ways, all the numbers can be selected
# O(n * log n)
def numberOfWays(arr):
    arr.sort()
    n = 1
    for i in range(len(arr)):
        # using binary search, find the number of elements
        # that are less than the current number.
        # than subtract it with current number
        # multiplication is to find all possible variations
        n *= bisect.bisect_right(arr, i) - i

    return n

for i in xrange(int(raw_input())):
    raw_input()
    arr = list(map(int, raw_input().split()))
    print numbers(arr) % 1000000007