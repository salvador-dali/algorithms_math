# https://www.hackerrank.com/challenges/easy-sum
# divide the sum into the two parts - the one from the integer part and remainder.
# for example 1, 2, 3, 4, 5, 6, 7, 8
# and modular by 3 you can see that the part 1, 2, 3 and 4, 5, 6 are the same.
def easySum(n, m):
    part, remainder, s = n / m, n % m, 0

    if part:
        s += (m * (m - 1) / 2) * part

    if remainder:
        s += remainder * (remainder + 1) / 2

    return s

for i in xrange(input()):
    n, m = map(int, raw_input().split())
    print easySum(n, m)

