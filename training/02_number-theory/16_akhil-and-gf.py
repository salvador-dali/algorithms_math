# https://www.hackerrank.com/challenges/akhil-and-gf/
# notice that 1..11 with n ones can be written as (10^n - 1) / 9 = a / 9
# taking the mod from this number (knowing that a divisible by 9 fully)
# (10^n - 1) mod (9 * k). And after this because the number is divisible by 9, divide it by 9
def only_ones(n, k):
    a = (pow(10, n, 9 * k) - 1) % (9 * k)
    return a / 9

for i in xrange(input()):
    print only_ones(*map(int, raw_input().split()))