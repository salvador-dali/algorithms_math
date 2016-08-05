# https://www.hackerrank.com/challenges/even-odd-query
# check 3 possibilities:
# if Arr[a] is odd, then the answer will be odd as well,
# the only difference is when a == b then the answer is even
# if Arr[a + 1] == 0 then the answer is odd
def even_odd(arr, a, b):
    if arr[a - 1] % 2 or (a != b and arr[a] == 0):
        return 'Odd'
    else:
        return 'Even'

input()
arr = list(map(int, raw_input().split()))
for i in xrange(input()):
    a, b = map(int, raw_input().split())
    print even_odd(arr, a, b)