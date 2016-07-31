# https://www.hackerrank.com/challenges/closest-number
# if the b is negative, the answer is either 0 or 1
# if the b is positive, then it depends on the whether the residual
# is bigger or smaller then x/ 2
def closest(a, b, x):
    if b < 0:
        tmp = 0
        if x == 1:
            return 1
    else:
        tmp = a**b

    m = tmp % x
    if m < x / 2.0:
        return tmp - m
    else:
        return tmp - m + x


for i in xrange(input()):
    a, b, x = map(int, raw_input().split())
    print closest(a, b, x)