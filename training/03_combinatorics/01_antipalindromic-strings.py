# https://www.hackerrank.com/challenges/antipalindromic-strings/
# the substring contains a palindrom if the palindrom is of size 2 or 3
# First of all if the length of string is 1, then we can select m words
# if the length is 2: m * (m - 1).
# if 3: m * (m - 1) * (m - 2)
# now is it is 4, the forth element can be selected also m - 2 possible ways
# because you can not select only previous two characters.
# so the answer is m * (m - 1) * (m - 2)^(n-2)

def antipalindrom(n, m, mod):
    if n == 1:
        return m % mod

    if n == 2:
        return m * (m - 1) % mod

    return m * (m - 1) * pow(m - 2, n - 2, mod) % mod

for i in xrange(input()):
    n, m = map(int, raw_input().split())
    print antipalindrom(n, m, 10**9 + 7)