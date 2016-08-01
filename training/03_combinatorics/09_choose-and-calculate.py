"""
https://www.hackerrank.com/challenges/choose-and-calculate
Number of ways to select k elements out of m is C(k, m).
Let's sort the array of elements so a1 <= a2 <= ... <= an
Now in each of the pairs we are interested in the smallest and biggest element

The number of occurrences follows the diagonal of the pascal triangle
"""
mod = 10**9 + 7

def generatePascalDiagonal(n, m):
    arr, m = [1], m - 1
    for i in xrange(m, n - 1):
        arr.append(arr[-1] * (i + 1) / (i + 1 - m))

    return arr

def calcSum(arr, m):
    arr.sort()
    diag = [i % mod for i in generatePascalDiagonal(len(arr), m)]
    s = 0
    for i in xrange(len(arr), m - 1, -1):
        s = (s + arr[i - 1] * diag[i - m]) % mod

    for i in xrange(len(arr) - m + 1):
        s = (s - arr[i] * diag[len(diag) - i - 1]) % mod

    return s % mod

n, m = map(int, raw_input().split())
arr = map(int, raw_input().split())

print calcSum(arr, m)