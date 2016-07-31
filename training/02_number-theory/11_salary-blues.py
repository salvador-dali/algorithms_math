# https://www.hackerrank.com/challenges/salary-blues
# first thing to notice is that the result of all manipulations is gcd
# gcd(A1, A2, ... An)
# if to add K to it, it will result in a different number
# gcd(A1 + K, A2 + K, ..., An + K)
# if to subtract first value from each other value (except of the first), you will get:
# gcd(A1 + K, A2 - A1, ..., An - A1)
# notice that the similar thing is for the first formula:
# gcd(A1, A2 - A1, ... An - A1)
#
# precalculating gcd(A2 - A1, ..., An - A1) = b
# then you need to do the following queries
# gcd(A1, b)
# gcd(A1 + K, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_multiple(arr):
    return reduce(gcd, arr)

def salary(arr_numbers, arr_q):
    arr_numbers.sort()
    if len(arr_numbers) == 1:
        for i in arr_q:
            print arr_numbers[0] + i

        return 1

    for i in xrange(1, len(arr_numbers)):
        arr_numbers[i] -= arr_numbers[0]

    x = gcd_multiple(arr_numbers[1:])
    for _ in arr_q:
        print gcd(x, arr_numbers[0] + _)

n, q = map(int, raw_input().split())
arr_numbers = list(map(int, raw_input().split()))
arr_q = [input() for i in xrange(q)]
salary(arr_numbers, arr_q)