# https://www.hackerrank.com/contests/infinitum11/challenges/check-gcd
# if there is a subset, whose GCD is equal to k, then all numbers from that
# subset should be divisible by k.
#
# so the first step is to reduce the number of all numbers to only numbers which are divisible by k
# and to transform all of them to num/k (we need only unique elements).
#
# After the gcd of these all numbers is not 1, it means that they all have some other divisor as well

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_multiple(arr):
    return reduce(gcd, arr)


def main(arr, k):
    arr2 = list({i / k for i in arr if i % k == 0})
    if not len(arr2):
        return 'NO'
    if gcd_multiple(arr2) == 1:
        return 'YES'
    else:
        return 'NO'


for i in xrange(input()):
    _, k = map(int, raw_input().split())
    print main(list(map(int, raw_input().split())), k)